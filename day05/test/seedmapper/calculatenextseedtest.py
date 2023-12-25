import unittest
from calculatenextseed import CalculateNextSeed

class CalculateNextSeedTest(unittest.TestCase):
    def setUp(self):
        self.calc = CalculateNextSeed()
        self.map=dict()
        self.map["name"]="test map"
        self.map["map"]=[[0,39,15],[15,0,37],[52,37,2]]


    def test_nextseed1(self):
        self.assertEqual(39,self.calc.calc(self.map, 0))

    def test_nextseed2(self):
        self.assertEqual(40,self.calc.calc(self.map, 1))

    def test_nextseed2(self):
        self.assertEqual(53,self.calc.calc(self.map, 14))

    def test_nextseed3(self):
        self.assertEqual(0,self.calc.calc(self.map, 15))

    def test_nextseed4(self):
        self.assertEqual(1,self.calc.calc(self.map, 16))

    def test_nextseed5(self):
        self.assertEqual(36,self.calc.calc(self.map, 51))

    def test_nextseed6(self):
        self.assertEqual(37,self.calc.calc(self.map, 52))

    def test_nextseed7(self):
        self.assertEqual(38,self.calc.calc(self.map, 53))

    def test_nextseed8(self):
        self.assertEqual(54,self.calc.calc(self.map, 54))

    def test_nextseed9(self):
        map=dict()
        map["name"]="test map"
        map["map"]=[[50,52,48],[98,50,2]]
        self.assertEqual(0,self.calc.calc(map, 0))
        self.assertEqual(49,self.calc.calc(map, 49))
        self.assertEqual(52,self.calc.calc(map, 50))
        self.assertEqual(99,self.calc.calc(map, 97))
        self.assertEqual(50,self.calc.calc(map, 98))
        self.assertEqual(51,self.calc.calc(map, 99))
        self.assertEqual(100,self.calc.calc(map, 100))

    #self.map["name"]="test map"
    #self.map["map"]=[[0,39,15],[15,0,37],[52,37,2]]

    def test_notInMap(self):
        self.assertEqual([[100,150]],self.calc.calcRange(self.map, [100,150]))

    def test_PartInRow(self):
        self.assertEqual([[1,31]],self.calc.calcRange(self.map, [16,46]))

    def test_FullRange(self):
        self.assertEqual([[37,38]],self.calc.calcRange(self.map, [52,53]))

    def test_UpperBoundNormal(self):
        self.assertEqual([[38,38],[54,55]],self.calc.calcRange(self.map, [53,55]))

    def test_LowerBoundOut(self):
        self.assertEqual([[35,36],[37,38]],self.calc.calcRange(self.map, [50,53]))

    def test_SeveralRange(self):
        self.assertEqual([[0,36],[37,38],[54,60]],self.calc.calcRange(self.map, [15,60]))

    def test_SeveralRange(self):
        map=dict()
        map["name"]="test map"
        map["map"]=[[50,52,48],[98,50,2]]
        self.assertEqual([[52,99],[50,51],[0,49],[100,150]],self.calc.calcRange(map, [0,150]))

    def test_SeveralRange(self):
        map=dict()
        map["name"]="test map"
        map["map"]=[[50,52,48],[98,50,2]]
        self.assertEqual([[52,99],[50,51],[0,49],[100,150]],self.calc.calcRange(map, [0,150]))