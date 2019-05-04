from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from SklearnVersionDataset import SklearnVersionDataset

S = SklearnVersionDataset()
stringDataset, cls = S.get()

print("特征提取中")
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(stringDataset)

mnb = MultinomialNB()
mnb.fit(X, cls)
predict = mnb.predict(X)
print(mnb.score(X, cls))
print(classification_report(cls, predict))
