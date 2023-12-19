import unittest
from calculatecardcopies import CalculateCardCopies

class CalculateCardCopiesTest(unittest.TestCase):
    def test_SumCardsCopiesWithoutExtraCopy(self):
        cards=[]
        cards.append(self.generate0ScoreCards())
        cards.append(self.generate0ScoreCards())
        cards.append(self.generate0ScoreCards())

        self.assertEqual(3,CalculateCardCopies().sumCopies(cards))

    def test_SumCardsCopiesWithCopies1(self):
        cards=[]
        cards.append(self.generate1ScoreCards()) #1
        cards.append(self.generate1ScoreCards()) #1+1
        cards.append(self.generate1ScoreCards()) #1+2
        cards.append(self.generate0ScoreCards()) #1+3
        cards.append(self.generate0ScoreCards()) #1

        self.assertEqual(11,CalculateCardCopies().sumCopies(cards))

    def test_SumCardsCopiesWithCopies2(self):
        cards=[]
        cards.append(self.generate16ScoreCards()) #1
        cards.append(self.generate16ScoreCards()) #1+1=2
        cards.append(self.generate16ScoreCards()) #1+1+2=4
        cards.append(self.generate0ScoreCards()) #1+1+2+4=8
        cards.append(self.generate0ScoreCards()) #1+1+2+4=8
        cards.append(self.generate0ScoreCards()) #1+1+2+4=8
        cards.append(self.generate0ScoreCards()) #1+2+4=7
        cards.append(self.generate0ScoreCards()) #1+4=5

        self.assertEqual(43,CalculateCardCopies().sumCopies(cards))

    def generate0ScoreCards(self):
        return "Card 1: 11 12 13 14 15 |  8  7  6  5  4  3  2  1"

    def generate1ScoreCards(self):
        return "Card 1: 11 12 3 14 15 |  8  7  6  5  4  3  2  1"

    def generate16ScoreCards(self):
        return "Card 1:  1  2 3  4  5 |  8  7  6  5  4  3  2  1"