import time
from loggercontext import LoggerContext
from calculateseeds import CalculateSeeds
from dtoparser import DtoParser

class Interactor():
    logger = LoggerContext()

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self):
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        dtoParser=DtoParser()
        dtoParser.parse(fileContent.splitlines())
        calculateSeeds=CalculateSeeds()
        result = calculateSeeds.calculate(dtoParser.getSeeds(), dtoParser.getMaps())

        self.logger.info("calculated seeds:"+str(result))
        print(min(result))

    def runRange(self):
        start_time = time.time()
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        dtoParser=DtoParser()
        dtoParser.parse(fileContent.splitlines())
        calculateSeeds=CalculateSeeds()

        result = calculateSeeds.calculateRange(dtoParser.getSeeds(), dtoParser.getMaps())


        print(min(result)[0])
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed time: ", elapsed_time)



