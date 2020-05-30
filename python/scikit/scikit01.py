#https://tellusxdp.github.io/start-python-with-tellus/lesson6.html
from sklearn import datasets



#3.2 学習に使うデータセットをインポートする
irisdata = datasets.load_iris()

print(irisdata.data)

#「0」「1」「2」のいずれかの値になっており、
# それぞれ「Setosa」「Versicolor」「Virginica」
print(irisdata.target)

print(irisdata.data.shape)
print(irisdata.target.shape)


print(irisdata.feature_names)
print(irisdata.target_names)


#3.4 データを訓練データとテストデータに分ける
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(irisdata.data, irisdata.target, test_size = 0.2, train_size = 0.8, shuffle = True)


#3.5 モデルを作って学習する
from sklearn.svm import SVC

classifier = SVC(kernel = "linear", gamma = "scale")

classifier.fit(X_train, y_train)


#3.6 期待する性能が出たかを評価する
y_pred = classifier.predict(X_test)

print("y_pred")
print(y_pred)

print("y_test")
print(y_test)

from sklearn import metrics

print(metrics.accuracy_score(y_test, y_pred))

print("混同行列")
print(metrics.confusion_matrix(y_test, y_pred))


print("正答率")
print(metrics.classification_report(y_test, y_pred))