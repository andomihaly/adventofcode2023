from loggercontext import LoggerContext
from boatracetactics import BoatRaceTactics

class Interactor():
    logger = LoggerContext()

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self):
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        #business logic
        self.logger.info("sum is calculated:"+str("result"))
        print("result")



