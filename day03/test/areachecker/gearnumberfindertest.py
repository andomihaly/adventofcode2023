import unittest
from gearnumberfinder import GearNumberFinder


class GearNumberFinderTest(unittest.TestCase):

    def setUp(self):
        self.gearNumberFinder = GearNumberFinder()

    def test_NoNumber(self):
        self.assertEqual(0, len(self.gearNumberFinder.findGearNumber(".....",".....",".....")))

    def test_NoNumber2(self):
        self.assertEqual(0, len(self.gearNumberFinder.findGearNumber(".....","..40*",".....")))
        self.assertEqual(0, len(self.gearNumberFinder.findGearNumber(".....","..*40",".....")))
        self.assertEqual(0, len(self.gearNumberFinder.findGearNumber("...40","....*",".....")))
        self.assertEqual(0, len(self.gearNumberFinder.findGearNumber(".....","....*","...40")))
        self.assertEqual(0, len(self.gearNumberFinder.findGearNumber("40...","*....",".....")))
        self.assertEqual(0, len(self.gearNumberFinder.findGearNumber(".....","*...","40...")))

    def test_SimpleCase(self):
        self.assertEqual([34,10], self.gearNumberFinder.findGearNumber("........","..34*10.","........")[0])

    def test_aboveBelow(self):
        self.assertEqual([34,10], self.gearNumberFinder.findGearNumber("...34...","...*....","...10...")[0])

    def test_above(self):
        self.assertEqual([10,34], self.gearNumberFinder.findGearNumber("...34...","...*10..","........")[0])

    def test_above2(self):
        self.assertEqual([34,10], self.gearNumberFinder.findGearNumber(".34.10..","...*....","........")[0])

    def test_below(self):
        self.assertEqual([10,34], self.gearNumberFinder.findGearNumber("........","...*10..","....34..")[0])

    def test_below2(self):
            self.assertEqual([10,34], self.gearNumberFinder.findGearNumber("........","...*....",".10.34..")[0])

    def test_corner(self):
        self.assertEqual([10,34], self.gearNumberFinder.findGearNumber(".10.....","...*....","....34..")[0])

    def test_corner2(self):
        self.assertEqual([10,34], self.gearNumberFinder.findGearNumber("....10..","...*....",".34.....")[0])

    def test_moreStars(self):
        self.assertEqual([10,34], self.gearNumberFinder.findGearNumber("....10..","...*...*",".34....5")[0])

    def test_midleNumbers(self):
        self.assertEqual([12345,54321], self.gearNumberFinder.findGearNumber(".12345..","...*...*",".54321.5")[0])

    def test_oneDigitCase1(self):
        self.assertEqual([6,5], self.gearNumberFinder.findGearNumber("....6...","...*....","..5.....")[0])

    def test_oneDigitCase2(self):
        self.assertEqual([6,5], self.gearNumberFinder.findGearNumber("...6....","...*....","...5....")[0])
    def test_moreGears(self):
        self.assertEqual([10,34], self.gearNumberFinder.findGearNumber("....10.6","...*...*",".34....5")[0])
        self.assertEqual([6,5], self.gearNumberFinder.findGearNumber("....10.6","...*...*",".34....5")[1])