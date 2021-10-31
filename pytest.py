import re
import argparse
from pathlib import Path
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", metavar="", type=Path, help="Path for log file")
parser.add_argument("-w", "--word", metavar="", type=str, help="What to look for, either string or regex")
if len(sys.argv) == 1:
    sys.exit("No arguments passed, -h for help. Execution aborted.")
argsParsed = parser.parse_args()
try:
    re.compile(argsParsed.word)
    regex_valid = True
    regMask = re.compile(argsParsed.word)
# re.I,re.M
# (^.*\.+log$)|(^.*\.+txt$)
except re.error:
    regex_valid = False
if not argsParsed.filepath:
    sys.exit("Please provide filepath. Execution aborted.")
fPath = argsParsed.filepath

if os.path.isfile(fPath):
    foundFiles = 1
    with open(fPath) as file:
        lines = file.readlines()
    file.close()
    with open(r"C:\Users\poluhin\Desktop\pypy\output.txt", "w") as outFile:
        for l in lines:
            if regMask.search(l):
                print("Found a match:  ", l)
                outFile.write(l)
    outFile.close()
#re.findall
elif os.path.isdir(fPath):
    foundFiles = 2
    txtMask = re.compile(r"^.*\.+txt$", re.IGNORECASE)
    dirFiles = os.listdir(fPath)
    with open(r"C:\Users\poluhin\Desktop\pypy\output.txt", "w") as outFile:
        for curFile in dirFiles:
            with open(curFile) as cFile:
                if cFile.search(txtMask):
                    lines = cFile.readlines()
                    for l in lines:
                        if regMask.search(l):
                            outFile.write(l)
    outFile.close()
else:
    foundFiles = 0
    sys.exit("\nFiles/path not found. Execution aborted.")