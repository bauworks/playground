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