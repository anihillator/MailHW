import re
import argparse
from pathlib import Path
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filepath", metavar="", type=Path, help="Path for log file")
argsParsed = parser.parse_args()
fPath=argsParsed.filepath
if os.path.isfile(fPath):
    foundFiles=1
    print("\nThat's a file!\n")
    with open(fPath) as file:
        lines = file.readlines()
    for l in lines
        
elif os.path.isdir(fPath):
    foundFiles=1
    print("\nThat's a directory!\n")
    dirFiles=os.listdir(fPath)
else:
    foundFiles=0
    print("Not found\n")