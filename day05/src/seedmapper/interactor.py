from loggercontext import LoggerContext
from calculateseeds import CalculateSeeds
from dtoparser import DtoParser

class Interactor():
    logger = LoggerContext()

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self):
        print(self.logger)
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        dtoParser=DtoParser()
        dtoParser.parse(fileContent.splitlines())
        calculateSeeds=CalculateSeeds()
        result = calculateSeeds.calculate(dtoParser.getSeeds(), dtoParser.getMaps())

        self.logger.info("sum is calculated:"+str(result))
        print(min(result))



