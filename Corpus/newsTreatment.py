import os

try:
    path = os.getcwd() + "\\Corpus\\"
    getError = os.listdir(path)
except FileNotFoundError:
    path = os.getcwd() + "\\Cabueta-FakeNewsDetection\\Corpus\\"

try:
    openFile = open(path + "normalizedData.txt", "r", encoding="utf-8")
except FileNotFoundError:
    openFile = open(path + "normalizedData.txt", "w", encoding="utf-8")
    openFile.close()

def insertIntoNormalizedFile(pathFunc, label):
    files = os.listdir(pathFunc)
    for file in files:
        if file.endswith(".txt"):
            openFile = open(pathFunc + file, "r", encoding="utf-8")
            content = openFile.readlines()
            content = str(content)[2:-2]
            content = content.replace("\n", " ")
            openFile.close()

            openFile = open(path + "normalizedData.txt", "a", encoding="utf-8")
            openFile.write(label + content + '\n')
            openFile.close()

pathFake = path + "fake\\"
pathTrue = path + "true\\"

insertIntoNormalizedFile(pathFake, "__label__Fake	")
insertIntoNormalizedFile(pathTrue, "__label__NotFake	")
