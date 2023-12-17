from loggercontext import LoggerContext
from game import Game
from color import Color

class GameParser():
    logger = LoggerContext()
    def parsAGame(self, text):
        subTexts=text.split(": ")
        game = Game(subTexts[0])
        game.gameTurns = self.getTurns(subTexts[1])
        print (game.gameTurns)
        return game

    def getTurns(self, text):
        subTexts=text.split("; ")
        dices = []
        for oneTurn in subTexts:
            self.logger.debug("one turn text:"+oneTurn)
            dices.append(self.getTurn(oneTurn))
        return dices

    def getTurn(self, text):
        rawDices = text.split(", ")
        self.logger.debug(rawDices)
        dices = self.createATrunContainer()
        for rawDice in rawDices:
            diceContent = rawDice.split(" ")
            dices[self.getColor(diceContent[1])]=int(diceContent[0])
        self.logger.debug(dices)
        return dices

    def createATrunContainer(self):
        dicesContainer = dict()
        for elemet in Color:
            dicesContainer[elemet]=0
        return dicesContainer

    def getColor(self, color):
        self.logger.debug("color to parse:" + color)
        return Color[str.upper(color)]