import pandas as pd
import numpy as np
from dataRead import wordList, classDict, wordD, words
import jieba
import os

class Bayes(object):
    def __init__(self, wordList, wordD, words):
        self.wordList = np.array(wordList)
        self.wordD = wordD

        self.words = words
        self.sum = np.sum(self.wordList, 0)
        self.filterList = ["，","。","、","？","；","：","“","”","‘","’","（","）","【","】","《","》","！", " ","-","~"]
    def analyse(self, filePath):
        self.file = open(filePath, "r", encoding="gbk", errors="ignore").read()
        self.file = self.file.replace("\n", " ")
        W = jieba.cut(self.file)
        W = list(W)
        possibilities = [1] * len(self.wordList)
        for word in W:
            if word in words:
                try:
                    index = words[word]
                except:
                    continue
                for i in range(len(self.wordList)):
                    possibilities[i] *= (self.wordList[i][index+1]+1)/self.sum[index+1]
                s = sum(possibilities)
                possibilities = [i/s for i in possibilities]
        # for i in range(len(self.wordList)):
        #     p = 1
        #     for word in W:
        #         if word in words:
        #             try:
        #                 index = words[word]
        #             except:
        #                 continue
        #             # if self.wordList[i][index+1]>0:
        #                 # print(p, self.wordList[i][index+1])
        #             p *= ((self.wordList[i][index+1]+0.1)/self.sum[index+1]+ 0.5)
        #     possibilities.append(p)
        # s = sum(possibilities)
        # possibilities = [i / s for i in possibilities]
        possibilities = np.array(possibilities)
        index = np.where(possibilities == np.max(possibilities))[0]
        print(possibilities)
        return self.wordD[index[0]], possibilities[index[0]]



bayes = Bayes(wordList, wordD, words)


datasetDir = "./dataset"
classL = os.listdir(datasetDir)
classDict = {}
for i in classL:
    classDict[i] = 0
classList = [os.path.join(datasetDir, i) for i in classL if os.path.isdir(os.path.join(datasetDir, i)) and i.find("C")>=0]

index = 0
resultDict = {

}
for i in classList:
    # print(index)
    currentClass = classL[index]
    fileList = os.listdir(i)
    fileList = [os.path.join(i, j) for j in fileList if j.find(".txt")>=0]
    for F in fileList:
        print(F)
        try:
            cls, score = bayes.analyse(F)
            resultDict[F] = (cls, score)
            print(resultDict[F])
        except:
            pass
    index += 1
# 记录
file = open("BayesResult.txt", "w")
for i in resultDict:
    try:
        file.write("{0}:{1}\n".format(i, resultDict[i]))
    except:
        print("###### ",i, resultDict)
file.close()



