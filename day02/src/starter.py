import sys
import os

parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)
sys.path.append(parent_dir+"\\cubegamechecker")
sys.path.append(parent_dir+"\\loader")
sys.path.append(parent_dir+"\\logger")
from textfileloader import TextFileLoader
from interactor import Interactor
from color import Color

if __name__ == '__main__':
    folderOfFiles ="loader\\";
    fileName = "example.txt"
    #fileName = "advent_day2_e1.txt"
    tfl= TextFileLoader(folderOfFiles +fileName)
    dices=dict()
    dices[Color.RED]=12;
    dices[Color.GREEN]=13;
    dices[Color.BLUE]=14;
    interactor = Interactor(tfl)
    interactor.run(dices)
    interactor.runPowerOfMinimumDices()
