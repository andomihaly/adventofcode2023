import unittest
from findnumberwithborder import FindNumberWithBorder


class FindNumberWithBorderTest(unittest.TestCase):

    def setUp(self):
        self.border = FindNumberWithBorder()

    def test_NoNumber(self):
        self.assertEqual(0, len(self.border.findBorderedNumbers(".....",".....",".....")))

    def test_NoNumber2(self):
        self.assertEqual(0, len(self.border.findBorderedNumbers(".....","..5..",".....")))
        self.assertEqual(0, len(self.border.findBorderedNumbers(".....","-.5.*",".....")))

    def test_NoNumber3(self):
        self.assertEqual(0, len(self.border.findBorderedNumbers(".....",".5.5.",".....")))

    def test_easyNumberBefore(self):
        result = self.border.findBorderedNumbers(".....",".$32.",".....")
        self.assertEqual(1, len(result))
        self.assertEqual(32, result[0])

    def test_easyNumberAfter(self):
        result = self.border.findBorderedNumbers(".....",".34/.",".....")
        self.assertEqual(1, len(result))
        self.assertEqual(34, result[0])

    def test_easyNumberInSpecialPosition(self):
        result = self.border.findBorderedNumbers(".....","..$32",".....")
        self.assertEqual(1, len(result))
        self.assertEqual(32, result[0])
        result = self.border.findBorderedNumbers(".....","34/..",".....")
        self.assertEqual(1, len(result))
        self.assertEqual(34, result[0])

    def test_twoNumberInRow(self):
        result = self.border.findBorderedNumbers(".....","3/.(5",".....")
        self.assertEqual(2, len(result))
        self.assertEqual(3, result[0])
        self.assertEqual(5, result[1])

    def test_leftTopCorner(self):
        result = self.border.findBorderedNumbers("%....",".34..",".....")
        self.assertEqual(1, len(result))
        self.assertEqual(34, result[0])

    def test_rightTopCorner(self):
        result = self.border.findBorderedNumbers("...%.",".34..",".....")
        self.assertEqual(1, len(result))
        self.assertEqual(34, result[0])

    def test_leftBottomCorner(self):
        result = self.border.findBorderedNumbers(".....",".34..","!....")
        self.assertEqual(1, len(result))
        self.assertEqual(34, result[0])

    def test_rightBottomCorner(self):
        result = self.border.findBorderedNumbers(".....",".34..","...+.")
        self.assertEqual(1, len(result))
        self.assertEqual(34, result[0])

    def test_TopSide(self):
        result = self.border.findBorderedNumbers(".*...",".34..",".....")
        self.assertEqual(1, len(result))
        self.assertEqual(34, result[0])

    def test_BottomSide(self):
        result = self.border.findBorderedNumbers(".....",".34..","..'..")
        self.assertEqual(1, len(result))
        self.assertEqual(34, result[0])

    def test_FullNumber(self):
        result = self.border.findBorderedNumbers(".****","12345","..'..")
        self.assertEqual(1, len(result))
        self.assertEqual(12345, result[0])

    def test_NumberInCorner(self):
        result = self.border.findBorderedNumbers(".1.1.","..3..",".4.4.")
        self.assertEqual(0, len(result))