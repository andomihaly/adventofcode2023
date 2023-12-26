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
        cardsWithJoker = parser.parseWithJoker(fileContent.splitlines())
        self.logger.info("content parsed")

        calculator = Calculator()
        result = calculator.calculate(cards)
        resultWithJoker=calculator.calculate(cardsWithJoker)
        self.logger.info("result is calculated:" + str(result))
        self.logger.info("result is calculated:" + str(resultWithJoker))
        print("Result: " + str(result))
        print("Result with Joker: " + str(resultWithJoker))