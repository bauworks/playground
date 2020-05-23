#https://tellusxdp.github.io/start-python-with-tellus/lesson2.html

import numpy as np

#3.1 array() でNumPyの配列を作る
a = np.array([0, 1, 2])
print(type(a))
print(a)
print(a.dtype)

b = np.array([1, 1.5, 2])
print(b)
print(b.dtype)

c = np.array([1 + 2j, 3 + 4j, 5 + 6j])
print(c)
print(c.dtype)

d = np.array([True, False, True, False, False])
print(d)
print(d.dtype)

e = np.array(list("TellusxData"))
print(e)
print(e.dtype)

#----------------------
# 主なNumPyのデータ型
#----------------------
# int8	正負ありの整数値（-128から127）
# int16	正負ありの整数値 (-32768から32767）
# int32	正負ありの整数値 (およそマイナス21億から21億）
# int64	正負ありの整数値 (およそマイナス922京から922京）
# uint8	正の数のみの整数値 (0から255)
# uint16	正の数のみの整数値 (0から65535)
# uint32	正の数のみの整数値 (0からおよそ42億）
# uint64	正の数のみの整数値 (0からおよそ1844京）
# float16	半精度と呼ばれる小数値
# float32	単精度と呼ばれる小数値
# float64	倍精度と呼ばれる小数値
f = np.array([10000, 20000, 30000, 40000], dtype = np.uint16)
print(f)
print(f.dtype)

g = np.array([1.4, 2.5, 3.6])
print(g)
print(g.dtype)

g = g.astype(np.int64)
print(g)
print(g.dtype)