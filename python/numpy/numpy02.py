#https://tellusxdp.github.io/start-python-with-tellus/lesson2.html 
import numpy as np

#配列の作成に関する便利なメソッド

#np.arange()
a = np.arange(20)
print(a)

b = np.arange(1, 21)
print(b)

c = np.arange(2, 41, 2)
print(c)

#np.linspace()
d = np.linspace(0, 10, 5)
print(d)

#np.empty()
e = np.empty(5)
print(e)

#np.zeros()とnp.ones()
f = np.zeros(5)
print(f)

f1 = np.ones(5)
print(f1)

#np.random.rand()
g = np.random.rand(5)
print(g)

#astypeで整数値に変換
g1 = g * 6 + 1
g1 = g1.astype(np.int8)
print(g1)

#配列を連結
#np.concatenate()
h = np.arange(1, 4) # [1,2,3]
i = np.arange(4, 7) # [4,5,6]
j = np.concatenate([h, i])
print(j)
