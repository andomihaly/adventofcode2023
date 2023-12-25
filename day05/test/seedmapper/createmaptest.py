import unittest
from createmap import CreateMap

class CreateMapTest(unittest.TestCase):
    def setUp(self):
        self.mapinput="50 98 2\n52 50 48\n"
    def test_parsemap(self):
        createmap = CreateMap()
        result = createmap.parseMapContent(self.mapinput.splitlines())
        self.assertEqual([[50,52,48],[98,50,2]],result)
    def test_parsemap(self):
        self.mapinput="seed-to-soil map:\n"+self.mapinput
        createmap = CreateMap()
        result = createmap.parseMap(self.mapinput.splitlines())
        self.assertEqual("seed-to-soil map",result["name"])
        self.assertEqual([[50,52,48],[98,50,2]],result["map"])
