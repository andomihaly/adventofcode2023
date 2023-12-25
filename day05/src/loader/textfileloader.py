from loggercontext import LoggerContext

class TextFileLoader():
    fileName = "NoFileSet.txt"
    logger = LoggerContext()

    def __init__(self, fileName):
        self.fileName = fileName
    def setInputFile(self, fileName):
        self.fileName = fileName
    def loadContent(self):
        self.logger.info("fajl beolvasasa: "+ self.fileName)
        f = open(self.fileName, "r")
        return f.read()
