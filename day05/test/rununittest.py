import unittest
import sys
import os
parent_dir = os.path.dirname(os.path.realpath(__file__))
root_dir=parent_dir.replace("\\test", "")
sys.path.append(root_dir+"\\src\\logger")
sys.path.append(root_dir+"\\src\\seedmapper")

from seedmapper.createmaptest import CreateMapTest
from seedmapper.calculatenextseedtest import CalculateNextSeedTest

if __name__ == '__main__':
    unittest.main()