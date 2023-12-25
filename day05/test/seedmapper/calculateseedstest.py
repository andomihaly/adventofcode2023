import unittest
from calculateseeds import CalculateSeeds

class CalculateSeedsTest(unittest.TestCase):
    def test_severalSeedsRange(self):
        map=dict()
        map["name"]="test map"
        map["map"]=[[56, 60, 37], [93, 56, 4]]
        maps=[map]
        #seeds=[[78, 80], [46, 56], [82, 85], [90, 98]]
        seeds=[78, 3, 46, 11, 82, 4, 90, 9]

        cs=CalculateSeeds()
        self.assertEqual([[82,84],[60,60],[46,55],[86,89],[94,96],[56,59],[97,98]],cs.calculateRange(seeds,maps))

