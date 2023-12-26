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
        cards = parser.parse(fileContent.splitlines())
        self.logger.info("content parsed")

        calculator = Calculator()
        result = calculator.calculate(cards)
        self.logger.info("result is calculated:" + str(result))
        print("Result: " + str(result))
