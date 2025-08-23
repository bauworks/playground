#各種ライブラリを宣言
import sys
import pandas as pd
import datetime
import time
import sqlite3
import fcntl
import numpy
import yfinance as yf
from decimal import Decimal, ROUND_HALF_UP
import math

dbname = 'STOCK_JP.db'


#---------------------------------------
# 小数点1桁に四捨五入
#---------------------------------------
def _r1_half_up(x):
    """小数点1桁に四捨五入。NaNはNoneにしてDBにNULL保存。"""
    if x is None:
        return None
    try:
        if isinstance(x, float) and math.isnan(x):
            return None
    except Exception:
        pass
    # numpy.float64 等も文字列経由で安全にDecimal化
    return float(Decimal(str(x)).quantize(Decimal('0.0'), rounding=ROUND_HALF_UP))


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
    """
    yfinance.download() の戻り値（複数銘柄を与えると列が MultiIndex になる）から、
    指定した `code`（例: "1301.T"）の OHLCV を1銘柄の DataFrame として取り出す。

    返り値:
      列: ['Open','High','Low','Close','Adj Close','Volume'] のうち存在するもの
      インデックス: 日付（DatetimeIndex）
    想定される列構造（yfinanceの挙動や引数 group_by によりブレがある）:
      A) (Ticker → Price)    例: ('1301.T','Open'), ('1301.T','High'), ...
      B) (Price  → Ticker)   例: ('Open','1301.T'), ('High','1301.T'), ...
      C) 単層列（1銘柄のみ取得時など） 例: 'Open','High',...
    """
    desired = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

    # --- C) 列が単層（= MultiIndex ではない）なら、そのまま必要列をそろえて返す ---
    if not isinstance(df_stockprice.columns, pd.MultiIndex):
        # 取得できた列だけを採用（Adj Close や Volume が欠けるケースにも耐える）
        cols = [c for c in desired if c in df_stockprice.columns]
        out = df_stockprice[cols].copy()
        # dtype を整える（Volume は int、それ以外は float を想定）
        cast = {c: ('int' if c == 'Volume' else 'float') for c in cols}
        return out.astype(cast, errors='ignore')

    # --- A/B) 列が MultiIndex の場合（yfinance の典型） ---
    level0_vals = df_stockprice.columns.get_level_values(0)
    level1_vals = df_stockprice.columns.get_level_values(1)

    # A) (Ticker → Price) パターン:
    #    先頭レベルが銘柄コード。print(df.columns.names) が ['Ticker','Price'] のようなケース。
    if code in level0_vals:
        # 欲しい列だけの MultiIndex を作り（例: [('1301.T','Open'), ...]）存在するものに絞る
        cols = pd.MultiIndex.from_product([[code], desired])
        cols = [c for c in cols if c in df_stockprice.columns]
        sub = df_stockprice.loc[:, cols].copy()
        # 列名を単層化: ('1301.T','Open') → 'Open'
        sub.columns = [c[1] for c in sub.columns]
        # 型整形
        cast = {c: ('int' if c == 'Volume' else 'float') for c in sub.columns}
        return sub.astype(cast, errors='ignore')

    # B) (Price → Ticker) パターン:
    #    先頭レベルが価格種別（Open/High/...）、第2レベルに銘柄コード。
    if code in level1_vals:
        # 欲しい列だけの MultiIndex を作成（例: [('Open','1301.T'), ...]）存在するものに絞る
        cols = pd.MultiIndex.from_product([desired, [code]])
        cols = [c for c in cols if c in df_stockprice.columns]
        sub = df_stockprice.loc[:, cols].copy()
        # 列名を単層化: ('Open','1301.T') → 'Open'
        sub.columns = [c[0] for c in sub.columns]
        cast = {c: ('int' if c == 'Volume' else 'float') for c in sub.columns}
        return sub.astype(cast, errors='ignore')

    # ここまで来たら、指定コードの列が見つからない（データ未取得・非上場・yfinance 側Error等）
    print(f'{code} not found in columns. Top-level samples: {sorted(set(level0_vals))[:5]} ...')
    return pd.DataFrame(columns=desired)


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
            _r1_half_up(row['Open']),
            _r1_half_up(row['High']),
            _r1_half_up(row['Low']),
            _r1_half_up(row['Close']),
            _r1_half_up(row['Adj Close']),
            None if pd.isna(row['Volume']) else int(row['Volume'])
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
    df_yahoo = yf.download(
        code_list,
        start=fromDate,
        end=toDate,
        group_by="ticker",
        auto_adjust=False 
    )

    #print(df_yahoo)
    #print(df_yahoo.columns.names)     # 例: ['Ticker', 'Price'] など
    #print(df_yahoo.columns[:8])       # 先頭8列のラベルを確認

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
sql += f' where "コード" between \'{fromCode}\' and \'{toCode}\' \n'
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
# 	code TEXT,
# 	date TEXT,
# 	"open" REAL,
# 	high REAL,
# 	low REAL,
# 	"close" REAL,
# 	adj_close REAL,
# 	volume INTEGER,
# 	CONSTRAINT TSE_PK PRIMARY KEY (code,date)
# );

# CREATE TABLE CODE (
# 	日付 TEXT(1),
# 	コード VARCHAR(4),
# 	銘柄名 VARCHAR(128),
# 	"市場・商品区分" VARCHAR(64),
# 	"33業種コード" VARCHAR(1),
# 	"33業種区分" VARCHAR(16),
# 	"17業種コード" VARCHAR(1),
# 	"17業種区分" VARCHAR(16),
# 	規模コード VARCHAR(1),
# 	規模区分 VARCHAR(16)
# );

#---------------------------------------
# JPX 東証上場銘柄一覧
#---------------------------------------
# https://www.jpx.co.jp/markets/statistics-equities/misc/01.html
