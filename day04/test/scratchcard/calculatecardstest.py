import unittest
from calculatecards import CalculateCards
class CalculateCardsTest(unittest.TestCase):
    def test_0sumCards(self):
        cards=[]
        cards.append(self.generate0ScoreCards())
        cards.append(self.generate0ScoreCards())
        cards.append(self.generate0ScoreCards())

        self.assertEqual(0,CalculateCards().sumWinningScore(cards))

    def generate0ScoreCards(self):
        return "Card 1: 11 12 13 14 15 |  8  7  6  5  4  3  2  1"

    def test_3sumCards(self):
        cards=[]
        cards.append(self.generate1ScoreCards())
        cards.append(self.generate1ScoreCards())
        cards.append(self.generate1ScoreCards())

        self.assertEqual(3,CalculateCards().sumWinningScore(cards))

    def generate1ScoreCards(self):
        return "Card 1: 11 12 3 14 15 |  8  7  6  5  4  3  2  1"

    def test_48sumCards(self):
        cards=[]
        cards.append(self.generate16ScoreCards())
        cards.append(self.generate16ScoreCards())
        cards.append(self.generate16ScoreCards())

        self.assertEqual(48,CalculateCards().sumWinningScore(cards))

    def generate16ScoreCards(self):
        return "Card 1:  1  2 3  4  5 |  8  7  6  5  4  3  2  1"