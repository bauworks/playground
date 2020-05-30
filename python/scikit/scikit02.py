#https://tellusxdp.github.io/start-python-with-tellus/lesson6.html

#4.1 実践1：手書き数字の画像の分類
from sklearn import datasets
digits = datasets.load_digits()

print("データセットの概要")
print(digits.DESCR)

X = digits.data
y = digits.target

print("データの個数")
print("X" + str(X.shape))
print("y" + str(y.shape))

print("データの中身")
print(X[0])
print(y[0:50])

import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()

#jupyter notebookなら表示できる
for i, x in enumerate(X[0:10], 0):
    sp = fig.add_subplot(2, 5, (i + 1))
    sp.imshow(x.reshape(8, 8), cmap = "gray")
    

#データを訓練データとテストデータに分ける
X_train = X[:1201]
X_test  = X[1201:]
y_train = y[:1201]
y_test  = y[1201:]


#モデルを作って学習する
from sklearn.svm import SVC
classifier = SVC(kernel = "linear", gamma = "scale")
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(y_pred)

print(y_test)

print("混同行列")
from sklearn import metrics
print(metrics.confusion_matrix(y_test, y_pred))

print("正答率")
print(metrics.classification_report(y_test, y_pred))

