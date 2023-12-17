from loggercontext import LoggerContext
from color import Color

class MinimumDicesCalculator():
    logger = LoggerContext()
    def calculate(self, game):
        minDices=self.createAContainer()
        self.logger.info(game.gameTurns)
        for turn in game.gameTurns:
            self.logger.info(turn)
            for elemet in Color:
                if (minDices[elemet]<turn[elemet]):
                    minDices[elemet]=turn[elemet]
        return minDices

    def createAContainer(self):
        container = dict()
        for elemet in Color:
            container[elemet]=0
        return container