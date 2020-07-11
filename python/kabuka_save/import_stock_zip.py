import os
import sys
import re
import zipfile
import sqlite3
import pandas as pd

if len(sys.argv) == 1:
    print("Usage: " + os.path.basename(sys.argv[0]) + " stock.zip")
    sys.exit()

# ZIPファイルPATH
zippath = sys.argv[1]

dirbase = os.path.splitext(zippath)[0]

# 解凍後のファイルPATH
txtpath =  dirbase + '.txt'

# ファイル名から株価コード取得
code = dirbase[dirbase.rfind('_') + 1:]


# ZIPファイル解凍
with zipfile.ZipFile(zippath) as zf:
    zf.extractall()


# 株価ファイル前処理（数値で始まる行のみを抽出）
codetsv = code + '.tsv'
with open( codetsv, mode='w') as wf:
    with open(txtpath) as rf:
        for rline in rf :
            if re.search('^[0-9]', rline):
                wf.write(rline)


# 株価ファイルをデータフレームに読み込む
df_tsv = pd.read_table(codetsv, index_col=0, names=('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'AdjClose'))
print(df_tsv.dtypes)
df_tsv.head(10)


# DB接続、インポート（無ければ新規に作成）
dbname = 'STOCK.db'
conn = sqlite3.connect(dbname)
df_tsv.to_sql('T' + code, conn, if_exists = 'replace')
# Option => if_exists　: append, replace, fail
conn.close()


