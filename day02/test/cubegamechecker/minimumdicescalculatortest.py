import unittest
from minimumdicescalculator import MinimumDicesCalculator
from game import Game
from color import Color

class MinimumDicesCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = MinimumDicesCalculator()
        self.game = Game("testgame")
        self.game.gameTurns=self.generateTurns()

    def test_normalGame(self):
        minDices=self.calculator.calculate(self.game)
        self.assertEqual(6,minDices[Color.RED] )
        self.assertEqual(5,minDices[Color.GREEN] )
        self.assertEqual(7,minDices[Color.BLUE] )

    def test_gameWithZero(self):
        turns=[]
        turns.append(self.generateTurn(3,0,5))
        self.game.gameTurns = turns
        minDices=self.calculator.calculate(self.game)
        self.assertEqual(3,minDices[Color.RED] )
        self.assertEqual(0,minDices[Color.GREEN] )
        self.assertEqual(5,minDices[Color.BLUE] )

    def generateTurns(self):
        turns=[]
        turns.append(self.generateTurn(6,3,4))
        turns.append(self.generateTurn(4,4,4))
        turns.append(self.generateTurn(4,5,7))
        return turns

    def generateTurn(self,red, green, blue):
        turn=dict()
        turn[Color.RED]=red
        turn[Color.GREEN]=green
        turn[Color.BLUE]=blue
        return turn

