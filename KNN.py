import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from SklearnVersionDataset import SklearnVersionDataset

class KNN(object):
    def __init__(self, K = 1):
        # 特征就不手动提取了
        S = SklearnVersionDataset()
        stringDataset, cls = S.get()
        self.cls = cls
        print("文件读取完毕")
        print("开始提取特征")
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(stringDataset)
        print("特征读取完成")
        # self.feature = X.toarray()
        self.feature = X.tocsr()
        # print(self.feature.shape)
        self.K = K
        self.clsSet = list(set(cls))
        self.clsDict = {}
        self.clsCount = {}
        for i in self.clsSet:
            self.clsDict[i] = i
            self.clsCount[i] = 0
    def cal(self):
        print("开始计算类别, K={0}".format(self.K))
        # 根据 a**2 + b**2 - 2ab
        file = open("KNNResult_K_{0}.txt".format(self.K), "w")
        a = self.feature.multiply(self.feature).sum(1)
        b = a.reshape(1, -1)
        c = self.feature.dot(self.feature.T)
        distance = a + b - 2*c
        # test_data_sq = self.feature.multiply(self.feature).sum(1)
        # train_data_sq = self.feature.multiply(self.feature).sum(1)
        # distance = test_data_sq.dot(train_data_sq.T)

        # num_test, num_train = distance.shape
        # distance = np.tile(test_data_sq, (1, num_test)) + np.tile(train_data_sq.T, (num_train, 1)) - 2 * distance

        topK_idx = np.argsort(distance)[:, 0:self.K]
        # topK_similarity = np.zeros((num_test, self.K), np.float32)
        # for i in range(num_test):
        #     topK_similarity = distance[i, topK_idx[i]]
        success = 0
        total = 0
        for i in range(topK_idx.shape[0]):
            result = topK_idx[i].copy()
            result.resize(result.shape[1])
            clsdict = self.clsCount.copy()
            # print(clsdict)
            for j in range(result.shape[0]):
                total += 1
                c = result[j]
                clsdict[self.cls[c]] += 1
            maxNum = 0
            maxCls = ""
            for j in clsdict:
                if clsdict[j] > maxNum:
                    maxNum = clsdict[j]
                    maxCls = j
            if maxCls == self.cls[i]:
                success+=1
            # print("file{0}: Truth:{1} Predict:{2}\n".format(i, self.cls[i], maxCls))
            file.write("file{0}: Truth:{1} Predict:{2}\n".format(i, self.cls[i], maxCls))
        file.close()
        print("K={0}, 准确率: {1}".format(self.K, success/total))
    def change(self, k):
        self.K = k

K = KNN(1)
K.cal()
K.change(2)
K.cal()
K.change(3)
K.cal()
K.change(4)
K.cal()
K.change(5)
K.cal()