#https://tellusxdp.github.io/start-python-with-tellus/lesson3.html

import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np


#グラフ1
y = np.random.rand(5)
y *= 5
plt.plot(y)
plt.show()



#グラフ2
x = np.arange(1, 11, 2)
y = np.random.rand(5)
y *= 5

plt.title('日本語タイトル')
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro']

plt.plot(x, y, linestyle = "--", marker = "^", color = "r")


plt.show()


# グラフ3
x = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
y = np.array([400, 300, 350, 450, 400, 600, 500, 450])

plt.title("Year - Count")
plt.xlabel("Year")
plt.ylabel("Count")
plt.grid(True)

plt.plot(x, y)

plt.show()



#3. 代表的なグラフの描き方
#3.1 棒グラフ
year = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
count = np.array([400, 300, 350, 450, 400, 600, 500, 450])

plt.bar(year, count)
plt.show()

#3.2 散布図
english = np.array([70, 95, 83, 100, 72, 71, 75, 85, 67, 75])
math = np.array([90, 82, 100, 95, 50, 81, 52, 56, 67, 71])

plt.scatter(english, math)

plt.show()


#3.3 円グラフ
fruits = np.array(["peach", "orange", "grape", "banana", "apple"])
count = np.array([12, 20, 34, 36, 47])

plt.pie(count, labels = fruits, autopct = "%.1f%%", startangle = 90)

plt.show()


#4. 複数のグラフを一度に表示する方法
#4.1 ひとつのグラフ領域に複数のグラフを描く
y1 = np.random.rand(11)
y2 = np.random.rand(11)

plt.plot(y1, color="blue", label = "y1")
plt.plot(y2, color="red", label = "y2")
plt.legend(loc = "upper left")
plt.show()


#4.2 複数のグラフを並べて表示する
y1 = np.random.rand(11)
y2 = np.random.rand(11)

fig = plt.figure()

sp1 = fig.add_subplot(1, 2, 1)
sp1.plot(y1)

sp2 = fig.add_subplot(1, 2, 2)
sp2.plot(y2)

plt.show()



#5. 応用例：近似直線の描き方
# サンプルデータ
x = np.array([20, 30, 40, 50, 60])
y = np.array([30, 38, 41, 49, 62])

# 近似直線の式の　a と b が入ったタプルを得る
p = np.polyfit(x, y, 1)

# 一次関数の式のオブジェクトを生成する
f = np.poly1d(p)

# 散布図と近似直線を描く
plt.scatter(x, y)
plt.plot(x, f(x))

plt.show()