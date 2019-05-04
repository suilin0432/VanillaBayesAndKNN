import os
import jieba
import pandas

# 给Bayes提供数据的数据处理

def wordRecord(wordsDict):
    dataFrame = pandas.DataFrame(wordsDict)
    filePath = "./wordDataset.csv"
    dataFrame.to_csv(filePath,sep=",",header=True,index=True,encoding="utf_8_sig")

datasetDir = "./dataset"
classL = os.listdir(datasetDir)
classDict = {}
for i in classL:
    classDict[i] = 0
classList = [os.path.join(datasetDir, i) for i in classL if os.path.isdir(os.path.join(datasetDir, i)) and i.find("C")>=0]
#PS: 1.编码格式是gbk等
#    2.三种可能的空格\u00A0,\u0020,\u3000 先替换成 空格然后在分割
print(classList)
decode = "GB2312"
# 过滤掉的标点符号等
wordFilter = ["，","。","、","？","；","：","“","”","‘","’","（","）","【","】","《","》","！", " ","-","~"]
wordsDict = {

}

index = 0
for i in classList:
    print(index)
    currentClass = classL[index]
    fileList = os.listdir(i)
    fileList = [os.path.join(i, j) for j in fileList if j.find(".txt")>=0]
    for F in fileList:
        print(F)
        file = open(F, "r", encoding="GBK", errors="ignore").read()
        # 去掉所有的\n
        file = file.replace("\n", " ")
        if len(file)==0:
            continue
        # 进行分词
        words = jieba.cut(file)
        for word in words:
            if word not in wordFilter:
                if word not in wordsDict:
                    wordsDict[word] = classDict.copy()
                    wordsDict[word][currentClass] = 1
                else:
                    wordsDict[word][currentClass] += 1
    index += 1

wordRecord(wordsDict)
# print(p)

