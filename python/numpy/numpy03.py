#https://tellusxdp.github.io/start-python-with-tellus/lesson2.html

import numpy as np

#3.3 多次元配列を作る

a = np.array([[1, 2, 3], [4, 5, 6]])
print("a=" + str(a))

a1 = np.empty((2, 3), dtype=np.int64)
a1[0] = [1, 2, 3]
a1[1] = [4, 5, 6]

print("a1=" + str(a1))


a2 = np.arange(1, 21)
print("a2=" + str(a2))
print("a2.shape=" + str(a2.shape))

b = a2.reshape(4, 5)
print("b=" + str(b))
print("b.shape=" + str(b.shape))


b2 = a2.reshape(2, 2, 5)
print("b2=", end="")
print(b2)
#print=("b2=" + str(b2))
#print=("b2.shape=" + str(b2.shape))


#多次元配列を1次元配列に変換するflatten()とravel()
#flatten() は必ず元の配列が残ります。ravel() は元の配列が無くなってしまう可能性があります。
#その代わり、ravel() の方が処理速度は高速です。
c = np.arange(1,21).reshape(4,5)
d = c.flatten()
print("c=", end="")
print(c)
print("d=", end="")
print(d)

e = c.ravel()
print("c=", end="")
print(c)
print("e=", end="")
print(e)
