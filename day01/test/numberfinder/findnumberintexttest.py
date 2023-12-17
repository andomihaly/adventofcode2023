import unittest
from findnumberintext import FindNumberInText


class FindNumberInTextTest(unittest.TestCase):

    def setUp(self):
        self.findNumber = FindNumberInText()
    def test_something(self):
        self.assertEqual(12, self.findNumber.findNumber("12"))


