import unittest
from cardparser import CardParser

class CardParserTest(unittest.TestCase):

    def test_parseACard(self):
        parser=CardParser()
        card=parser.pars("Card 1:  1  2  3  4  5 |  8  7  6  5  4  3  2  1")
        self.assertEqual("Card",card.name)
        self.assertEqual(1, card.id)
        self.assertEqual([1,2,3,4,5],card.numbers)
        self.assertEqual([8,7,6,5,4,3,2,1],card.winningNumbers)

    def test_parseAnotherCard(self):
        parser=CardParser()
        card = parser.pars("Card 14: 10 11  5 14 13 | 20 21 22 23 24  5 26 27")
        self.assertEqual("Card",card.name)
        self.assertEqual(14, card.id)
        self.assertEqual([10,11,5,14,13],card.numbers)
        self.assertEqual([20,21,22,23,24,5,26,27],card.winningNumbers)



