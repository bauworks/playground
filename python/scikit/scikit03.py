#https://tellusxdp.github.io/start-python-with-tellus/lesson6.html

#4.2 実践2：ビットコインの価格変動の予測

import pandas as pd
btc_price = pd.read_csv('coindesk-bpi-USD-close_data-2018-06-07_2018-06-27.csv')

head = btc_price.head(10)
print(head)

