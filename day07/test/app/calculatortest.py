import unittest

from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_one(self):
        calculator = Calculator()
        self.assertEqual(-1, calculator.calculate())
