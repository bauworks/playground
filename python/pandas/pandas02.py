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


#4. DataFrameとndarrayを相互変換する

#4.1 DataFrameからndarrayに変換する
nd_bank_data = bank_data.values

print(type(nd_bank_data))
print(nd_bank_data)

nd_bank_columns = bank_data.columns.values
print(type(nd_bank_columns))
print(nd_bank_columns)


#4.2 ndarrayからDataFrameに変換する
print("4.2")
re_bank_data = pd.DataFrame(data = nd_bank_data, columns = nd_bank_columns)

print(type(re_bank_data))
print(re_bank_data.head())

