import unittest
from findnumberintext import FindNumberInText


class FindNumberInTextTest(unittest.TestCase):

    def setUp(self):
        self.findNumber = FindNumberInText()
    def test_onlynumberbasic(self):
        self.assertEqual(12, self.findNumber.findNumber("12"))
    def test_onlynumbermoredigit(self):
        self.assertEqual(12, self.findNumber.findNumber("102"))
    def test_onlynumberonedigit(self):
        self.assertEqual(11, self.findNumber.findNumber("1"))

    def test_basicTestNumber(self):
        self.assertEqual(0, self.findNumber.findNumber("zero"))
        self.assertEqual(11, self.findNumber.findNumber("one"))
        self.assertEqual(22, self.findNumber.findNumber("two"))
        self.assertEqual(33, self.findNumber.findNumber("three"))
        self.assertEqual(44, self.findNumber.findNumber("four"))
        self.assertEqual(55, self.findNumber.findNumber("five"))
        self.assertEqual(66, self.findNumber.findNumber("six"))
        self.assertEqual(77, self.findNumber.findNumber("seven"))
        self.assertEqual(88, self.findNumber.findNumber("eight"))
        self.assertEqual(99, self.findNumber.findNumber("nine"))
    def test_mixedNumber(self):
        self.assertEqual(25, self.findNumber.findNumber("2nine5"))
        self.assertEqual(25, self.findNumber.findNumber("twonine5"))
        self.assertEqual(25, self.findNumber.findNumber("2ninefive"))
        self.assertEqual(25, self.findNumber.findNumber("twoninefive"))
    #special case
    def test_rollingtext2(self):
        self.assertEqual(22, self.findNumber.findNumber("twone"))
    def test_rollingtext0(self):
        self.assertEqual(0, self.findNumber.findNumber("zerone"))
    def test_rollingtext8with3(self):
        self.assertEqual(88, self.findNumber.findNumber("eighthree"))
    def test_rollingtext8with2(self):
        self.assertEqual(88, self.findNumber.findNumber("eightwo"))
    def test_rollingtext9(self):
        self.assertEqual(99, self.findNumber.findNumber("nineight"))
    def test_rollingtext93(self):
        self.assertEqual(93, self.findNumber.findNumber("nineighthree"))

    #complextest
    def test_complex(self):
        self.assertEqual(88, self.findNumber.findNumber("eighthreeightwo"))
        self.assertEqual(81, self.findNumber.findNumber("eighthreeightwone"))
        self.assertEqual(28, self.findNumber.findNumber("twoneightwo"))
        self.assertEqual(28, self.findNumber.findNumber("twoneightheeighthree"))
        self.assertEqual(23, self.findNumber.findNumber("twoneightheeigh4three"))
        self.assertEqual(78, self.findNumber.findNumber("sevenineighthree"))
        self.assertEqual(33, self.findNumber.findNumber("sthreeighthreeight"))
    def test_complex1(self):
        self.assertEqual(88, self.findNumber.findNumber("eighthreeighthree"))
    def test_complex2(self):
        self.assertEqual(33, self.findNumber.findNumber("sthreeighthreeight"))
