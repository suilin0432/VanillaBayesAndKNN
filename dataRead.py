import pandas as pd
dataFrame = pd.read_csv("./wordDataset.csv")
# dataFrame = pd.read_csv("./test.csv")
# ***记录反向映射表(根据类别找index)
classDict = {}
# ***这个是所有的词频list 纵坐标 类别号  横坐标 单词编号
wordList = [[0]*(len(dataFrame.keys())) for _ in range(len(dataFrame["Unnamed: 0"]))]
wordDict = dataFrame.to_dict()
keys = list(wordDict.keys())
# print(keys)
print(wordDict["Unnamed: 0"])

for i in wordDict["Unnamed: 0"]:
    classDict[wordDict["Unnamed: 0"][i]] = i
# ***正向记录映射表(根据index找类别)
wordD = wordDict["Unnamed: 0"]
# print(classDict)
words = {}
index = 0
for word in keys[1:]:
    words[word] = index
    index += 1
# print(words)
# 遍历所有的单词
for i in range(1, len(keys)):
    items = wordDict[keys[i]]
    # 遍历所有的 类别
    # print(items)
    for j in range(len(items)):
        wordList[j][i] = items[j]
# print(wordList)