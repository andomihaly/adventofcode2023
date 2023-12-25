from loggercontext import LoggerContext
from boatracetactics import BoatRaceTactics
from boatracesparser import BoatRacesParser

class Interactor():
    logger = LoggerContext()

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self):
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        #business logic
        bp=BoatRacesParser()
        races=bp.parse(fileContent.splitlines())
        brt=BoatRaceTactics()
        self.logger.info("races info:\t"+str(races))
        options=brt.findWinningOptionsInRaces(races)
        self.logger.info("races options:\t"+str(options))
        power = self.multipleWinningOptions(options)
        print(power)

    def runKerning(self):
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        #business logic
        bp=BoatRacesParser()
        races=bp.parseKerning(fileContent.splitlines())
        brt=BoatRaceTactics()
        self.logger.info("races info:\t"+str(races))
        options=brt.findWinningOptionsInRaces(races)
        power = self.multipleWinningOptions(options)
        print(power)

    def multipleWinningOptions(self, options):
        power = 1
        for option in options:
            power *= len(option)
        self.logger.info("multiplie number of race option:\t" + str(power))
        return power



