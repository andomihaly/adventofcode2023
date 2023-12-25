import unittest
from boatracesparser import BoatRacesParser

class BoatRacesParserTest(unittest.TestCase):
    def test_parseRace(self):
        input="Time:      1234\nDistance:  54321"
        bp=BoatRacesParser()
        result=bp.parse(input.splitlines())
        self.assertEqual(1, len(result))
        self.assertEqual([1234,54321], result[0])

    def test_parseRaces(self):
        input="Time:      1  22   33\nDistance:  5  66  777"
        bp=BoatRacesParser()
        result=bp.parse(input.splitlines())
        self.assertEqual(3, len(result))
        self.assertEqual([[1,5],[22,66],[33,777]], result)

    def test_parseRaces(self):
        input="Time:      1  22   33\nDistance:  5  66  777"
        bp=BoatRacesParser()
        result=bp.parseKerning(input.splitlines())
        self.assertEqual([[12233,566777]], result)