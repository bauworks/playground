#https://tellusxdp.github.io/start-python-with-tellus/lesson2.html

import numpy as np

print("#5. NumPyの配列の応用的な使い方")
print("#5.1 四則演算")


a = np.arange(1, 11)
print(a)
print(a + 1)
print(a - 1)
print(a * 2)
print(a / 2)
print(a % 2)

print("#配列同士")
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

print("-------")
print("a=", end="")
print(a)
print("b=", end="")
print(b)

print("[+]")
print(b + a)
print("[-]")
print(b - a)

print("-------")
c = np.arange(1, 5).reshape(2, 2)
d = np.arange(5, 9).reshape(2, 2)
print("c=", end="")
print(c)
print("d=", end="")
print(d)

print("[*]")
print(c * d)
print("[/]")
print(c / d)
print("[//]")
print(c // d)



print("5.2 ユニバーサル関数")

a = np.random.rand(5)
print(a)

a = a * 6 + 1

print(np.array(np.floor(a), dtype=np.int64))
print(np.array(np.ceil(a), dtype=np.int64))
print(np.array(np.round(a), dtype=np.int64))


print("5.3 行列の反転と回転")
a = np.arange(1, 10).reshape(3, 3)
print(a)

# 左右に反転させる            fliplr(配列)
b = np.fliplr(a)
print("b=", end="")
print(b)

# 上下に反転させる            flipud(配列)
c = np.flipud(a)
print("c=", end="")
print(c)

# 反時計回りに90度回転させる   rot90(配列, 1)
d = np.rot90(a, 1)
print("d=", end="")
print(d)

# 反時計回りに180度回転させる  rot90(配列, 2)
e = np.rot90(a, 2)
print("e=", end="")
print(e)

# 反時計回りに270度回転させる  rot90(配列, 3)
f = np.rot90(a, 3)
print("f=", end="")
print(f)
