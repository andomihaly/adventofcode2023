import unittest
from parser import Parser


class ParserTest(unittest.TestCase):
    def test_one(self):
        parser = Parser()
        self.assertEqual(0, parser.parse())
