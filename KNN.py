import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from SklearnVersionDataset import SklearnVersionDataset

class KNN(object):
    def __init__(self, K = 1):
        # 特征就不手动提取了
        S = SklearnVersionDataset()
        stringDataset, cls = S.get()
        print("文件读取完毕")
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(stringDataset)
        print("特征读取完成")
        self.feature = X.toarray()
        self.K = K
        self.clsSet = list(set(cls))
        self.clsDict = {}
        for i in self.clsSet:
            self.clsDict[i] = i
    def cal(self):
        print("开始计算类别")
        for i in self.feature:
            print(i)
            current = np.sum(np.multiply(i*self.feature), 1)
            print("1")
            k = sorted(enumerate(current), reverse=True, key=lambda x:x[1])
            print("2")
            k = k[:self.K]
            d = np.zeros((1, len(self.clsSet)))
            for i in k:
                d[self.clsDict[self.cls[i]]] += 1
            index = int(np.where(d==np.max(d)))
            print(self.clsSet[index])

K = KNN()
K.cal()