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
        self.assertEqual(0, len(self.border.findBorderedNumbers("555..","5.5.5","55...")))

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
        result = self.border.findBorderedNumbers(".....","..-32",".....")
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

    def test_FromProduction(self):
        a="............*....-..811..........846..855......*.............*..$........230.92@............................=.....................92........"
        b="..........360..........#....664.....=.*...881...677...934.780.......426.*..........8......654.....*959.....539..........21.........*........"
        c=".....................+.........*......379..*.........*.........=.........969........*........*.976..............872....*....../....579......"
        result = self.border.findBorderedNumbers(a,b,c)
        self.assertEqual(11, len(result))
        self.assertEqual(360, result[0])
        self.assertEqual(664, result[1])
        self.assertEqual(881, result[2])
        self.assertEqual(677, result[3])
        self.assertEqual(934, result[4])
        self.assertEqual(780, result[5])
        self.assertEqual(8, result[6])
        self.assertEqual(654, result[7])
        self.assertEqual(959, result[8])
        self.assertEqual(539, result[9])
        self.assertEqual(21, result[10])

    def test_similarNumber(self):
         result = self.border.findBorderedNumbers("$...","58..5",".....")
         self.assertEqual(1, len(result))
         self.assertEqual(58, result[0])

    def test_FromProduction2(self):
         a="...................*................*......214.134......................*805.%.....*.....*....*.....#.....*..........*....302.....934..=...."
         b="....835.........622..............8...541...*....*..861....442....874..........458...955...985..172.....497.310........341......$....*...644."
         c="....*......246......909....320.............893.150....*.....*....*........717................................................833.178........"
         result = self.border.findBorderedNumbers(a,b,c)
         self.assertEqual(14, len(result))




