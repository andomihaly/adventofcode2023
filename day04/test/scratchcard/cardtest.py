import unittest
from card import Card

class CardTest(unittest.TestCase):

    def test_0Hit(self):
        card=Card()
        card.numbers=[1,2,3,4,5]
        card.winningNumbers=[6,7,8,9,10,11,12,13]
        self.assertEqual(0, card.score())
    def test_1hit(self):
        card=Card()
        card.numbers=[1,2,3,4,5]
        card.winningNumbers=[5,7,8,9,10,11,12,13]
        self.assertEqual(1, card.score())

    def test_2hit(self):
        card=Card()
        card.numbers=[1,22,3,24,5]
        card.winningNumbers=[15,7,24,9,10,11,22,13]
        self.assertEqual(2, card.score())

    def test_3hit(self):
        card=Card()
        card.numbers=[1,22,3,24,25]
        card.winningNumbers=[25,7,24,9,10,11,22,13]
        self.assertEqual(4, card.score())
    def test_5hit(self):
        card=Card()
        card.numbers=[27,22,26,24,25]
        card.winningNumbers=[25,27,24,26,10,11,22,13]
        self.assertEqual(16, card.score())


