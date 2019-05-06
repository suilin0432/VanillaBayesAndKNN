import os
import jieba
import numpy as np

# 自己提取特征的效率很慢...

# KNN因为文件数目太多了... 提取了20000个单词作为计算 10000 * 20000
wordListFile = "./words.txt"
wordFile = open(wordListFile, "r", encoding="utf-8")
wordList = wordFile.readline().split(",")
wordDict = {}
# 建立字符和数组位置的映射
for i in range(len(wordList)):
    wordDict[wordList[i]] = i

# 开始统计单词频率矩阵
wordMatrix = np.zeros((9833, 20000)) # 9833个文件 20000个单词
# 记录文件名 和类别
fileMessage = []
# 记录的时候 每行 -> 文件名 类别 20000个单词出现的频率
datasetDir = "./dataset"
classL = os.listdir(datasetDir)

classList = [os.path.join(datasetDir, i) for i in classL if os.path.isdir(os.path.join(datasetDir, i)) and i.find("C")>=0]
index = 0
fi = 0
for i in classList:
    print(index)
    currentClass = classL[index]
    fileList = os.listdir(i)
    fileList = [os.path.join(i, j) for j in fileList if j.find(".txt")>=0]
    for F in fileList:
        print(F)
        fileMessage.append((F, currentClass))
        file = open(F, "r", encoding="GBK", errors="ignore").read()
        # 去掉所有的\n
        file = file.replace("\n", " ")
        if len(file)==0:
            continue
        # 进行分词
        words = jieba.cut(file)
        for word in words:
            if word in wordList:
               wordMatrix[fi][wordDict[word]] += 1
        fi += 1
        if fi > 5:
            break
    break
    index += 1
# 开始进行矩阵的记录:
recordFile = open("KNNDataset.txt","w")
wordMatrix = wordMatrix.astype("<U6")
for i in range(len(fileMessage)):
    print(i)
    recordFile.write("{0},{1},{2}\n".format(fileMessage[i][0],fileMessage[i][1],",".join(wordMatrix[i])))
recordFile.close()
# print(p)

