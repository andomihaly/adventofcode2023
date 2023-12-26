import os
import sys
import unittest

parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir + "\\test")
sys.path.append(parent_dir + "\\test\\app")
sys.path.append(parent_dir + "\\src\\app")
sys.path.append(parent_dir + "\\src\\logger")

from calculatortest import CalculatorTest
from parsertest import ParserTest

if __name__ == '__main__':
    unittest.main()
