import unittest
import sys
import os
parent_dir = os.path.dirname(os.path.realpath(__file__))
root_dir=parent_dir.replace("\\test", "")
sys.path.append(root_dir+"\\src\\scratchcard")
sys.path.append(root_dir+"\\src\\logger")

from scratchcard.cardtest import CardTest
from scratchcard.cardparsertest import CardParserTest
from scratchcard.calculatecardstest import CalculateCardsTest

if __name__ == '__main__':
    unittest.main()