import unittest
from boatracetactics import BoatRaceTactics

class BoatRaceTacticsTest(unittest.TestCase):
    def test_SimpleRace(self):
        race=[2,0]
        brt=BoatRaceTactics()
        result=brt.findWinningOptions(race)
        self.assertEqual([1],result)

    def test_MultipleWinningOption(self):
        race=[3,0]
        brt=BoatRaceTactics()
        result=brt.findWinningOptions(race)
        self.assertEqual([1,2],result)

    def test_someOptionIsNotWinningOption(self):
        race=[6,8]
        brt=BoatRaceTactics()
        result=brt.findWinningOptions(race)
        self.assertEqual([3],result)

    def test_someOptionIsNotWinningOption2(self):
        race=[6,7]
        brt=BoatRaceTactics()
        result=brt.findWinningOptions(race)
        self.assertEqual([2,3,4],result)

    def test_moreraces(self):
        races=[[6,7],[6,8]]
        brt=BoatRaceTactics()
        result=brt.findWinningOptionsInRaces(races)
        self.assertEqual([[2,3,4],[3]],result)

    def test_morerace(self):
        races=[[6,7],[6,10]]
        brt=BoatRaceTactics()
        result=brt.findWinningOptionsInRaces(races)
        self.assertEqual([[2,3,4],[]],result)