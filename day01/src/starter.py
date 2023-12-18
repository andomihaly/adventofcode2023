import sys
import os

parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)
sys.path.append(parent_dir+"\\numberfinder")
sys.path.append(parent_dir+"\\loader")
sys.path.append(parent_dir+"\\logger")
from textfileloader import TextFileLoader
from interactor import Interactor

if __name__ == '__main__':
    folderOfFiles ="loader\\";
    fileName = "example.txt"
    #fileName = "advent_day1_e1.txt"

    tfl= TextFileLoader(folderOfFiles +fileName)
    interactor = Interactor(tfl)
    interactor.run()
