#各種ライブラリを宣言
import sys
import pandas as pd
from pandas_datareader import data as pdr
import datetime
import time
import sqlite3
import fcntl
import numpy
import yfinance as yfin
yfin.pdr_override()

dbname = 'STOCK_JP.db'

#---------------------------------------
# 証券コード一覧を取得
#---------------------------------------
def sql_fetchall(sql):
    # DBオープン
    conn = sqlite3.connect(dbname)

    # SQL実行
    cur = conn.cursor()
    cur.execute(sql)
    sql_result = cur.fetchall()

    # DBクローズ
    conn.close()

    return sql_result

#---------------------------------------
# 取得した株価データから特定銘柄のみピックアップ
#---------------------------------------
def pick_code_data(df_stockprice, code):

    # マルチインデックスでなければそのままリターン
    if df_stockprice.columns[0] == 'Open':
        # Single Index
        return df_stockprice
    
    # 集約用の空のデータフレームを生成
    columns_list = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    dfpick_list = pd.DataFrame(data=[], index=[], columns=columns_list)

    # LOOP: Yahooから取得した株価データ（日付）
    for index, row in df_stockprice.iterrows():

        # データを取得できていなかったらスキップ
        if numpy.isnan(row['Open'][code]) == True:
            print(f'{code} Skip. [{index}](NaN)')
            continue;

        # 指定銘柄のデータをピックアップ
        pick = [[ row['Open'][code]
                , row['High'][code]
                , row['Low'][code]
                , row['Close'][code]
                , row['Adj Close'][code]
                , row['Volume'][code]
                ]]

        # ピックアップしたデータをデータフレームに変換
        dfpick = pd.DataFrame(data=pick, index=[index], columns=columns_list)

        # データフォーマットを設定
        dfpick = dfpick.astype({'Open':'float','High':'float','Low':'float','Close':'float','Adj Close':'float','Volume':'int'})

        # 今回のデータを集約用データフレームに連結
        dfpick_list = pd.concat([dfpick_list, dfpick])

    return dfpick_list


#---------------------------------------
# 株価データをDBに登録
#---------------------------------------
def register_stockprice(df_stockprice, code, fromDate, toDate):

    ### LOOP:株価データ件数 ###
    for index, row in df_stockprice.iterrows():

        # 範囲外のデータならスキップ
        if f'{index:%Y-%m-%d}' < fromDate or f'{index:%Y-%m-%d}' > toDate:
            print(f'{code} Skip. [{index}]')
            continue

        # DBオープン
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()

        #SQL作成
        cur = conn.cursor()
        sql = 'insert into TSE(code, date, open, high, low, close, adj_close, volume) values(?,?,?,?,?,?,?,?)'
        param = [
            code.replace(".T", ""),
            f'{index:%Y-%m-%d}',
            row['Open'],
            row['High'],
            row['Low'],
            row['Close'],
            row['Adj Close'],
            row['Volume']
            ]

        #SQL実行
        try:
            cur.execute(sql, param)
            conn.commit()
            print(str(code) + " Success." + str(param))
        except:
            print(str(code) + " SQL Error." + str(param))

        # DBクローズ
        conn.close()


#---------------------------------------
# 銘柄リストの株価データを取得＆DB登録
#---------------------------------------
def get_and_register(code_list, fromDate, toDate):
    #---------------------------------------
    # 株価データ取得（Yahoo!ファイナンス）
    #---------------------------------------
    df_yahoo = pdr.get_data_yahoo(code_list, start=fromDate, end=toDate)
    # print(df_yahoo)

    #---------------------------------------
    # 取得した株価データを銘柄単位でDB登録
    #---------------------------------------
    # LOOP: 銘柄コードリスト
    for code in code_list:
        # LOOP銘柄のデータのみをピックアップ
        df_pick_list = pick_code_data(df_yahoo, code)
        # print(code)
        # print(df_pick_list)

        # ピックアップした株価データをDBに登録
        register_stockprice(df_pick_list, code, fromDate, toDate)



##############################################
### MAIN START ###############################
##############################################
# 引数のチェックと取得(引数２つ以下はエラー)
if(len(sys.argv) <= 2+1):
    print(f'Usage: {sys.argv[0]} From-code To-code from-Date(YYYY-MM-DD) [to-Date(YYYY-MM-DD)]')
    sys.exit()

#---------------------------------------
# 銘柄コードの範囲を決定 
#---------------------------------------
fromCode = sys.argv[1]
toCode = sys.argv[2]

#---------------------------------------
# 日付範囲を決定 
#---------------------------------------
# 引数が３つの場合はToをargv[3]とする
if(len(sys.argv) == 3+1):
    fromDate = sys.argv[3]
    toDate = sys.argv[3]
else:
    fromDate = sys.argv[3]
    toDate = sys.argv[4]

# Toの日付を取得範囲に含めるために1日進める
dtTo = datetime.datetime.strptime(toDate, '%Y-%m-%d')   #日付型に変換
dtTo = dtTo + datetime.timedelta(days=1)  #翌日を取得
toDate = dtTo.strftime('%Y-%m-%d')

print(f'Date: [ {fromDate} ]-[ {toDate} ]')
print(f'Code: [ {fromCode} ]-[ {toCode} ]')


#---------------------------------------
# 銘柄コードリストを取得 
#---------------------------------------
# コードリスト取得SQL
sql = ''
sql += f'select distinct "コード" \n'
sql += f'  from CODE \n'
sql += f' where "コード" between {fromCode} and {toCode} \n'
sql += f'   and "33業種コード" <> \'-\' \n'
sql += f'   and "市場・商品区分" <> \'PRO Market\' \n'
if(len(sys.argv) == 3+1):
    sql += f'   and "コード" not in (select code from TSE where date = \'{fromDate}\') \n'
sql += f' order by "コード"'

# 検索実行
print(sql)
code_list = sql_fetchall(sql)
#print(code_list)

# SQL結果を銘柄コードの配列に変換
tse_list = [ str(code[0]) + ".T" for code in code_list]
print(tse_list)


#---------------------------------------
# 1ロット(=10銘柄)でDB登録
#---------------------------------------
lot_code_list = []
for code in tse_list:
    # ロットに銘柄コードを追加
    lot_code_list.append(code)

    # 10銘柄になったらDB登録処理の呼び出し
    if len(lot_code_list) >= 10:
        # 株価取得&DB登録
        get_and_register(lot_code_list, fromDate, toDate)

        # ロットを初期化
        lot_code_list = []

# 端数ロットのDB登録呼び出し
if len(lot_code_list) > 0:
    get_and_register(lot_code_list, fromDate, toDate)


print(f'Done.[{fromDate}][{fromCode}][{toCode}]')


#---------------------------------------
# DDL
#---------------------------------------
# CREATE TABLE TSE (
# 	code INTEGER,
# 	date TEXT,
# 	"open" REAL,
# 	high REAL,
# 	low REAL,
# 	"close" REAL,
# 	adj_close REAL,
# 	volume INTEGER,
# 	CONSTRAINT TSE_PK PRIMARY KEY (code,date)
# );
# CREATE UNIQUE INDEX sqlite_autoindex_TSE_1 ON TSE (code,date);

# CREATE TABLE CODE (
# 	日付 TEXT(1),
# 	コード INTEGER,
# 	銘柄名 VARCHAR(128),
# 	"市場・商品区分" VARCHAR(64),
# 	"33業種コード" VARCHAR(1),
# 	"33業種区分" VARCHAR(16),
# 	"17業種コード" VARCHAR(1),
# 	"17業種区分" VARCHAR(16),
# 	規模コード VARCHAR(1),
# 	規模区分 VARCHAR(16)
# );