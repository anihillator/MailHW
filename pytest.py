import re
import argparse
from pathlib import Path
import sys
import os
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
    sys.exit("Я не прикрутил поддержку плохого регекса, давайте заново.")
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
        for l in lines:
            for i in tqdm(range(100), desc='Progress', colour="#03A062"):
                if regMask.search(l):  # Looking for matches in every line
                    #  print("Found a match:  ", l)  # Print each match into console
                    outFile.write(l)  # Print each match into file
    outFile.close()
# re.search
elif os.path.isdir(fPath):
    foundFiles = 2
    txtMask = re.compile(r"(.*\.+log)|(.*\.+txt)", re.IGNORECASE)  # Filetypes to look for, e.g. (^.*\.+log$)|(^.*\.+txt$)
    dirFiles = os.listdir(fPath)  # All files in directory
    with open(r".\output.txt", "w") as outFile:
        for curFile in dirFiles:  # Current file from the list
            with open(os.path.join(fPath, curFile)) as cFile:  # Same as with single file, plus full path os.path.join(d, path)
                if txtMask.search(curFile):
                    outFile.write('\nFilename:{}\n'.format(curFile))
                    lines = cFile.readlines()
                    print('\nFilename:{}\n'.format(curFile))
                    for i in tqdm(range(100), desc='Progress', colour="#03A062"):
                        for l in lines:
                            if regMask.search(l):
                                outFile.write(l)
    outFile.close()
    print("\nDone!")
else:
    foundFiles = 0
    sys.exit("\nFiles/path not found. Execution aborted.")
