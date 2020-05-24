#https://tellusxdp.github.io/start-python-with-tellus/lesson4.html

import pandas as pd
import numpy as np

#bank.csv
# age           年齢
# job           職業
# marital       結婚した経験の有無
# education     最終学歴
# default       債務不履行かどうか
# balance       口座残高
# housing       住宅ローンの有無
# loan          パーソナルローンの有無
# contact       連絡手段
# day           最後に営業の連絡をした日にち（日）
# month         最後に営業の連絡をした日にち（月）
# duration      現在実施中のキャンペーンで最後に営業の連絡をした日からの経過日数
# campaign      現在実施中のキャンペーンで営業の連絡をした回数
# pdays         前回のキャンペーンで最後に営業の連絡をした日からの経過日数
# previous      前回のキャンペーンで営業の連絡をした回数
# poutcome      前回のキャンペーンでの結果
# y             定期預金の契約の有無


bank_data = pd.read_csv("bank.csv")

print(type(bank_data))


#3. データを参照・表示する
#3.1 とりあえず表示する
print(bank_data)

print("HEAD")
print(bank_data.head(10))

print("TAIL")
print(bank_data.tail(10))


#3.2 スライス
#位置の数値でスライスする
print(bank_data.iloc[1, 1])    # 1番目のみ
print(bank_data.iloc[0:3, 0:3])   # 0番目から4番目まで
print(bank_data.iloc[:11:2, :11:2])    # 先頭から12番目まで（増分2で）

print(bank_data.iloc[100:110, :10])


#列名でスライスする
print(bank_data.loc[1, "job"])
print(bank_data.loc[0:2, ["age", "job", "marital"]])
print(bank_data.loc[:10:2, ["age", "marital", "default", "housing", "contact", "month"]])

