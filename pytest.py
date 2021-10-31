import re
import argparse
from pathlib import Path
import sys
import os
from time import sleep
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", metavar="", type=Path, help="Path the log file")
parser.add_argument("-w", "--word", metavar="", type=str, help="What to look for, either string or regex")
if len(sys.argv) == 1:  # No args passed
    sys.exit("No arguments passed, -h for help. Execution aborted.")
argsParsed = parser.parse_args()
try:
    re.compile(argsParsed.word)
    regex_valid = True
    regMask = re.compile(argsParsed.word)
# re.I,re.M
#
except re.error:
    regex_valid = False
if not argsParsed.filepath:
    sys.exit("Please provide filepath. Execution aborted.")
fPath = argsParsed.filepath

if os.path.isfile(fPath):  # If given path is a file
    foundFiles = 1
    with open(fPath) as file:
        lines = file.readlines()
    file.close()
    with open(r".\output.txt", "w") as outFile:  # Create output file
        print('Filename:{}'.format(fPath))
        for i in tqdm(range(100), desc='Progress', colour="#03A062"):
            for l in lines:
                if regMask.search(l):  # Looking for matches in every line
                    #  print("Found a match:  ", l)  # Print each match into console
                    outFile.write(l)  # Print each match into file
    outFile.close()
# re.search
elif os.path.isdir(fPath):
    foundFiles = 2
    txtMask = re.compile(r"(^.*\.+log$)|(^.*\.+txt$)",
                         re.IGNORECASE)  # Filetypes to look for, e.g. (^.*\.+log$)|(^.*\.+txt$)
    dirFiles = os.listdir(fPath)  # All files in directory
    with open(r".\output.txt", "w") as outFile:
        for curFile in dirFiles:  # Current file from the list
            with open(curFile) as cFile:  # Same as with single file
                if cFile.search(txtMask):
                    lines = cFile.readlines()
                    for l in lines:
                        if regMask.search(l):
                            outFile.write(l)
    outFile.close()
else:
    foundFiles = 0
    sys.exit("\nFiles/path not found. Execution aborted.")
