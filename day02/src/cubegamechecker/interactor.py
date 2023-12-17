from loggercontext import LoggerContext
from gameparser import GameParser
from color import Color
from minimumdicescalculator import MinimumDicesCalculator

class Interactor():
    logger = LoggerContext()

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self, numberOfDices):
        self.logger.info("process started")
        self.numberOfDices = numberOfDices
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        #business logic
        sumOfIDs=self.sumGameIdIfPossible(fileContent)
        self.logger.info("sum is calculated:"+str(sumOfIDs))
        print(sumOfIDs)

    def runPowerOfMinimumDices(self):
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        #business logic
        power=self.powerOfMinimumDices(fileContent)
        self.logger.info("sum is calculated:"+str(power))
        print(power)

    def sumGameIdIfPossible(self, games):
        games = games.splitlines()
        gameParser = GameParser()
        sumOfId=0
        for gameText in games:
            self.logger.info("next: " + gameText)
            game=gameParser.parsAGame(gameText)
            if (not self.isGameFalse(game)):
                self.logger.info("game is ok: "+str(game.gameID))
                sumOfId+=game.gameID
        return sumOfId

    def isGameFalse(self, game):
        for turn in game.gameTurns:
            self.logger.debug("game turn:\t"+str(turn))
            for actualColor in Color:
                self.logger.debug("color \t: "+str(actualColor)+" dice:\t"+str(turn[actualColor])+ " have: \t"+str(self.numberOfDices[actualColor]))
                if turn[actualColor]>self.numberOfDices[actualColor]:
                    return True
        return False

    def powerOfMinimumDices(self,games):
        games = games.splitlines()
        gameParser = GameParser()
        minimumDicesCalculator=MinimumDicesCalculator()
        sumOfPower=0
        for gameText in games:
            self.logger.info("next: " + gameText)
            game=gameParser.parsAGame(gameText)
            minimumDices=minimumDicesCalculator.calculate(game)
            sumOfPower+=self.calculatePower(minimumDices)
        return sumOfPower

    def calculatePower(self,minimumDices):
        power=1
        for elemet in Color:
            if (minimumDices[elemet]>0):
                power *= minimumDices[elemet]
        return power


