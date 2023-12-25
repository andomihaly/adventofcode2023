import unittest
import sys
import os
parent_dir = os.path.dirname(os.path.realpath(__file__))
root_dir=parent_dir.replace("\\test", "")
sys.path.append(root_dir+"\\src\\boatrace")
sys.path.append(root_dir+"\\src\\logger")

from boatrace.boatracesparsertest import BoatRacesParserTest
from boatrace.boatracetacticstest import BoatRaceTacticsTest

if __name__ == '__main__':
    unittest.main()