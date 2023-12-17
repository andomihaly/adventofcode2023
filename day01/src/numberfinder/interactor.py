from loggercontext import LoggerContext
from findnumberintext import FindNumberInText

class Interactor():
    logger = LoggerContext()

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self):
        print(self.logger)
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        total = self.calculateAndSum(fileContent)
        self.logger.info("sum is calculated:"+str(total))
        print(total)

    def calculateAndSum(self, rows):
        rows = rows.splitlines()
        total = 0
        fnit=FindNumberInText()
        for row in rows:
            total += fnit.findNumber(row)
        return total

