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
        print("开始计算类别")
        # 根据 a**2 + b**2 - 2ab
        file = open("KNNResult.txt", "w")
        a = self.feature.multiply(self.feature).sum(1)
        b = a.reshape(1, -1)
        c = self.feature.dot(self.feature.T)
        print(a.shape)
        print(b.shape)
        print(c.shape)
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
        print(topK_idx.shape)
        for i in range(topK_idx.shape[0]):
            result = topK_idx[i].copy()
            result.resize(result.shape[1])
            print("i ", result)
            print(result.shape)
            clsdict = self.clsCount.copy()
            print(clsdict)
            for j in range(result.shape[0]):
                c = result[j]
                print("j", c)
                print(c.shape)
                clsdict[self.cls[c]] += 1
            maxNum = 0
            maxCls = ""
            for j in clsdict:
                if clsdict[j] > maxNum:
                    maxNum = clsdict[j]
                    maxCls = j

        # for i in topK_idx:
        #     print("i ",i)
        #     print(i.shape)
        #     clsdict = self.clsCount.copy()
        #     print(clsdict)
        #     for j in range(i.shape(0)):
        #         print("j ",j)
        #         print(j.shape)
        #         clsdict[self.cls[j]] += 1
        #     maxNum = 0
        #     maxCls = ""
        #     for j in clsdict:
        #         if clsdict[j] > maxNum:
        #             maxNum = clsdict[j]
        #             maxCls = j
            print("file{0}: Truth:{1} Predict:{2}\n".format(i, self.cls[i], maxCls))
            file.write("file{0}: Truth:{1} Predict:{2}\n".format(i, self.cls[i], maxCls))


        #
        # for i in self.feature:
        #     print(i)
        #     current = np.sum(np.multiply(i*self.feature), 1)
        #     print("1")
        #     k = sorted(enumerate(current), reverse=True, key=lambda x:x[1])
        #     print("2")
        #     k = k[:self.K]
        #     d = np.zeros((1, len(self.clsSet)))
        #     for i in k:
        #         d[self.clsDict[self.cls[i]]] += 1
        #     index = int(np.where(d==np.max(d)))
        #     print(self.clsSet[index])

K = KNN(3)
K.cal()