from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from SklearnVersionDataset import SklearnVersionDataset

S = SklearnVersionDataset()
stringDataset, cls = S.get()


# 进行特征提取
print("特征提取中")
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(stringDataset)
# 进行KNN分类 从最邻近 -> 5NN
for i in range(1, 6):
    K = KNeighborsClassifier(n_neighbors=i)
    K.fit(X, cls)
    predict = K.predict(X)
    print(K.score(X, cls))
    print(classification_report(cls, predict))