import os
import sys
import time

parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)
sys.path.append(parent_dir + "\\src\\app")
sys.path.append(parent_dir + "\\src\\loader")
sys.path.append(parent_dir + "\\src\\logger")

from textfileloader import TextFileLoader
from interactor import Interactor

if __name__ == '__main__':
    start_time = time.time()

    folderOfFiles = "src\\loader\\"
    fileName = "example.txt"
    # fileName = "puzzleinput.txt"
    tfl = TextFileLoader(folderOfFiles + fileName)
    interactor = Interactor(tfl)
    interactor.run()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time: ", elapsed_time)
