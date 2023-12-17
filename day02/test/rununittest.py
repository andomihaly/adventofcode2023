import unittest
import sys
import os
parent_dir = os.path.dirname(os.path.realpath(__file__))
root_dir=parent_dir.replace("\\test", "")
sys.path.append(root_dir+"\\src\\cubegamechecker")
sys.path.append(root_dir+"\\src\\logger")

from cubegamechecker.gameparsertest import GameParseTest

if __name__ == '__main__':
    unittest.main()