import os

class SklearnVersionDataset(object):
    def __init__(self):
        pass

    def get(self):
        datasetDir = "./dataset"
        classL = os.listdir(datasetDir)
        classDict = {}
        for i in classL:
            classDict[i] = 0
        classList = [os.path.join(datasetDir, i) for i in classL if
                     os.path.isdir(os.path.join(datasetDir, i)) and i.find("C") >= 0]

        # 文本集合
        stringDataset = []
        cls = []

        index = 0
        print("读取文件中")
        for i in classList:
            # print(index)
            currentClass = classL[index]
            fileList = os.listdir(i)
            fileList = [os.path.join(i, j) for j in fileList if j.find(".txt") >= 0]
            for F in fileList:
                # print(F)
                file = open(F, "r", encoding="gbk", errors="ignore").read()
                stringDataset.append(file)
                cls.append(currentClass)
            index += 1
        return stringDataset, cls