import unittest
from gameparser import GameParser


class FindNumberInTextTest(unittest.TestCase):

    def setUp(self):
        self.gameParser = GameParser()
    def test_title(self):
        self.assertEqual("Game 1", self.gameParser.parsAGame("Game 1:"))
