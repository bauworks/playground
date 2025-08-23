# StockPrice Downloader

東証上場銘柄コード一覧 (CODE テーブル) を元に、指定範囲の銘柄コードの株価データを Yahoo Finance から取得し、SQLite に保存するスクリプトです。  
実験用に作成したものです。


## 必要環境

- Python 3.12
- SQLite3
- pip, venv


## セットアップ

```bash
# 仮想環境を作成
python -m venv .venv

# 仮想環境を有効化
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# 依存関係をインストール
pip install -r requirements.txt
```


### CODE テーブルの準備

JPX の「上場銘柄一覧」から最新の CSV をダウンロードして CODE テーブルを作成してください。
（JPX公式ページ から取得可能）

```sql
CREATE TABLE CODE (
  日付 TEXT,
  コード TEXT,
  銘柄名 TEXT,
  "市場・商品区分" TEXT,
  "33業種コード" TEXT,
  "33業種区分" TEXT,
  "17業種コード" TEXT,
  "17業種区分" TEXT,
  規模コード TEXT,
  規模区分 TEXT
);
```

### TSE テーブルの準備

株価データを格納するテーブルを作成します。

```sql
CREATE TABLE TSE (
  code TEXT,
  date TEXT,
  open REAL,
  high REAL,
  low REAL,
  close REAL,
  adj_close REAL,
  volume INTEGER,
  CONSTRAINT TSE_PK PRIMARY KEY (code,date)
);
```


## 使い方

```bash
$ source .venv/bin/activate
(.venv)$ python getstock3.py From-code To-code from-Date(YYYY-MM-DD) [to-Date(YYYY-MM-DD)]
```


例: 2025-08-22 の 1300～1310 番の銘柄コードを取得する場合

```bash
(.venv)$ python getstock3.py 1300 1310 2025-08-22
```

## 実行例

```bash
$ python getstock3.py 1300 1310 2025-08-22
Date: [ 2025-08-22 ]-[ 2025-08-23 ]
Code: [ 1300 ]-[ 1310 ]
select distinct "コード" 
  from CODE 
 where "コード" between '1300' and '1310' 
   and "33業種コード" <> '-' 
   and "市場・商品区分" <> 'PRO Market' 
   and "コード" not in (select code from TSE where date = '2025-08-22') 
 order by "コード"
['1301.T']
[*********************100%***********************]  1 of 1 completed
1301.T Success.['1301', '2025-08-22', 4850.0, 4935.0, 4835.0, 4895.0, 4895.0, 104300]
Done.[2025-08-22][1300][1310]
```



## このまま運用する場合のヒント
-	仮想環境 .venv はリポジトリに含めず、.gitignore に追加する。
-	依存関係は requirements.in に最小限だけ書く（例: pandas, yfinance, pandas-datareader）。
-	pip-compile で requirements.txt を固定化し、環境を再現可能にする。

```bash
# requirements.in から requirements.txt を生成
pip-compile --generate-hashes --output-file=requirements.txt requirements.in

# 再現する場合
pip install -r requirements.txt
```



## 依存関係管理（このまま運用）
- requirements.in に最小限の依存関係を記述
- pip-compile で requirements.txt を生成（バージョン固定＋ハッシュ付き）
- pip-sync で環境を再現性ある形で同期

```bash
# 依存関係の追加
echo "newpackage" >> requirements.in
pip-compile --generate-hashes
pip-sync

# 依存関係の更新
pip-compile --upgrade --generate-hashes
pip-sync
```

常に pip-sync を使って環境を合わせること。pip install ではなく pip-sync を推奨します。


## 参考
- 東証銘柄一覧: https://www.jpx.co.jp/markets/statistics-equities/misc/01.html
- データ取得: yfinance

