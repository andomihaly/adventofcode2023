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
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        dtoParser=DtoParser()
        dtoParser.parse(fileContent.splitlines())
        calculateSeeds=CalculateSeeds()
        seeds=[]
        seedInRange=dtoParser.getSeeds()
        for index in range(0,len(seedInRange),2):
            for seed in range(seedInRange[index],seedInRange[index]+seedInRange[index+1]):
                seeds.append(seed)

        self.logger.info("number of seeds: "+str(len(seeds)))
        result = calculateSeeds.calculate(seeds, dtoParser.getMaps())

        self.logger.info("calculated seeds:"+str(result))
        print(min(result))



