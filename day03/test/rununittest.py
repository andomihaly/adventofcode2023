import unittest
import sys
import os
parent_dir = os.path.dirname(os.path.realpath(__file__))
root_dir=parent_dir.replace("\\test", "")
sys.path.append(root_dir+"\\src\\areachecker")
sys.path.append(root_dir+"\\src\\logger")

from areachecker.findnumberwithbordertest import FindNumberWithBorderTest
from areachecker.gearnumberfindertest import GearNumberFinderTest

if __name__ == '__main__':
    unittest.main()