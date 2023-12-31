from loggercontext import LoggerContext
from calculatecards import CalculateCards
from calculatecardcopies import CalculateCardCopies

class Interactor():
    logger = LoggerContext()

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self):
        print(self.logger)
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        #business logic
        result = CalculateCards().sumWinningScore(fileContent.splitlines())

        self.logger.info("sum is calculated:"+str(result))
        print(result)

    def runCopies(self):
        print(self.logger)
        self.logger.info("copies process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        #business logic
        result = CalculateCardCopies().sumCopies(fileContent.splitlines())

        self.logger.info("sum copied card is calculated:"+str(result))
        print(result)



