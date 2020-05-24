#https://tellusxdp.github.io/start-python-with-tellus/lesson2.html

import numpy as np

print("#4.1 NumPyの配列を使う")
a = np.arange(1, 101).reshape(10, 10)
print(a[0, 0])            # 0番目のみ
print(a[1, 1])            # 1番目のみ
print(a[1:3, 1:3])        # 1番目から2番目まで
print(a[1:5:3, 1:5:3])    # 1番目から4番目まで（増分3で）
print(a[:5, :5])          # 先頭から4番目まで
print(a[7:, 7:])          # 7番目から末尾まで
print(a[::3, ::3])        # 先頭から末尾まで（増分3で）
print(a[:, :])            # 全体（先頭から末尾まで）」


print("#4.2 要素の新規追加")
print("a=")
a = np.arange(1, 20)
print(a)
a = np.append(a, 20)
print(a)
a = np.append(a, (21, 22, 23, 24))
print(a)

print("b=", end="")
b = np.arange(1, 6)
b = np.insert(b, 1, 6)
b = np.insert(b, 3, (7, 8))
print("b=", end="")
print(b)


print("多次元配列")
a = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
b = np.array([1, 1, 1])
b1 = np.array([1, 2, 3, 4])

#配列aの縦と横の要素数を取得
#（このように書くことで変数hには縦の要素数3、変数vには横の要素数3が格納される）
(h, v) = a.shape
print("h=", end="")
print(h)
print("v=", end="")
print(v)

print("# 上から2行目に1行追加")
c = np.insert(a, 2, b, 0)
print(c)

print("# 縦の末尾に1行追加")
d = np.insert(a, h, b, 0)
print(d)

print("# 左から2列目に1列追加")
e = np.insert(a, 2, b1, 1)
print(e)

print("# 横の末尾に1列追加")
f = np.insert(a, v, b1, 1)
print(f)


print("#4.3 要素の削除")
a = np.arange(5)
a = np.delete(a, 2)
print(a)

print("# 1行目を削除")
b = np.arange(1, 26).reshape(5, 5)
b = np.delete(b, 1, 0)
print(b)

print("# 1列目を削除")
c = np.arange(1, 26).reshape(5, 5)
c = np.delete(c, 1, 1)
print(c)


print("3次元")
z = np.arange(1, 25).reshape(2, 3, 4)
print("z=", end="")
print(z)

z1 = np.insert(z, 2, [0, 0, 0, 0], 1)
print("z1=", end="")
print(z1)

z2 = np.insert(z, 2, [0, 0, 0], 2)
print("z2=", end="")
print(z2)

# z方向にinsertは出来る？
#z3 = np.insert(z, 1, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 3)
#print("z3=", end="")
#print(z3)

