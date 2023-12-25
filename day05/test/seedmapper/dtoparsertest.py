import unittest
from dtoparser import DtoParser

class DtoParserTest(unittest.TestCase):
    def test(self):
        input="seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15"
        dtoparser = DtoParser()
        dtoparser.parse(input.splitlines())
        self.assertEqual([79,14,55,13], dtoparser.getSeeds())

        self.assertEqual(2, len(dtoparser.getMaps()))
        self.assertEqual("seed-to-soil map", dtoparser.getMaps()[0]["name"])
        self.assertEqual([[50,52,48],[98,50,2]], dtoparser.getMaps()[0]["map"])
        self.assertEqual("soil-to-fertilizer map", dtoparser.getMaps()[1]["name"])
        self.assertEqual([[0,39,15],[15,0,37],[52,37,2]], dtoparser.getMaps()[1]["map"])

