import unittest
from gameparser import GameParser
from color import Color

class GameParseTest(unittest.TestCase):

    def setUp(self):
        self.gameParser = GameParser()

    def test_parseAGameTurn(self):
        game = self.gameParser.parsAGame("Game 1: 3 blue, 4 red")
        self.assertEqual("Game 1", game.gameName)
        self.assertEqual(1, len(game.gameTurns))
        self.assertEqual(3, len(game.gameTurns[0]))
        self.assertEqual(4, game.gameTurns[0][Color.RED])
        self.assertEqual(3, game.gameTurns[0][Color.BLUE])
        self.assertEqual(0, game.gameTurns[0][Color.GREEN])

    def test_parseAnotherGameTurn(self):
        game = self.gameParser.parsAGame(" : 10 red, 20 green, 60 blue")
        self.assertEqual(10, game.gameTurns[0][Color.RED])
        self.assertEqual(60, game.gameTurns[0][Color.BLUE])
        self.assertEqual(20, game.gameTurns[0][Color.GREEN])

    def test_parseSameColorGameTurn(self):
        game = self.gameParser.parsAGame(" : 5 red")
        self.assertEqual(5, game.gameTurns[0][Color.RED])
        self.assertEqual(0, game.gameTurns[0][Color.BLUE])
        self.assertEqual(0, game.gameTurns[0][Color.GREEN])

    def test_parseMultipleGameTurns(self):
        game = self.gameParser.parsAGame(" : 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(3, len(game.gameTurns))
        self.assertEqual(4, game.gameTurns[0][Color.RED])
        self.assertEqual(3, game.gameTurns[0][Color.BLUE])
        self.assertEqual(0, game.gameTurns[0][Color.GREEN])
        self.assertEqual(1, game.gameTurns[1][Color.RED])
        self.assertEqual(6, game.gameTurns[1][Color.BLUE])
        self.assertEqual(2, game.gameTurns[1][Color.GREEN])
        self.assertEqual(0, game.gameTurns[2][Color.RED])
        self.assertEqual(0, game.gameTurns[2][Color.BLUE])
        self.assertEqual(2, game.gameTurns[2][Color.GREEN])