class TextFileLoader():
    fileName = "NoFileSet.txt"
    # fileName = "advent_day1_e1.txt"
    def __init__(self, fileName):
        self.fileName = fileName
    def setInputFile(self, fileName):
        self.fileName = fileName
    def loadContent(self):
        f = open(self.fileName, "r")
        return f.read()