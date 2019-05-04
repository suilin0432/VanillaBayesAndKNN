file = open("BayesResult.txt", "r")
line = file.readline()
success = 0
total = 0
cls = ["C39-","C38-","C37-","C36-","C35-","C34-","C32-","C31-","C29-","C23-","C19-","C17-","C16-","C15-","C11-","C7-","C6-","C5-","C4-","C3-"]
while line:
    total += 1
    begin, end = line.split(":")
    for i in cls:
        if i in begin and i in end:
            success += 1
            break
    line = file.readline()
print("正确概率: {0}%".format(success/total*100))
