from loggercontext import LoggerContext
from calculator import Calculator
from parser import Parser

class Interactor():
    logger = LoggerContext()

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self):
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")

        # business logic
        parser = Parser()
        network = parser.parse(fileContent.splitlines())
        route = parser.parsePath(fileContent.splitlines())
        self.logger.info("content parsed")

        calculator = Calculator()
        result = calculator.calculate(route, network)
        self.logger.info("result is calculated:" + str(result))
        print("Result: " + str(result))

    def runGhost(self):
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")

        # business logic
        parser = Parser()
        network = parser.parse(fileContent.splitlines())
        route = parser.parsePath(fileContent.splitlines())
        self.logger.info("content parsed")

        calculator = Calculator()
        result = calculator.calculateGhost(route, network)
        self.logger.info("result is calculated:" + str(result))
        print("Result: " + str(result))
