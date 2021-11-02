import re
import argparse
from pathlib import Path
import sys
import os
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--filepath", metavar="", type=Path, help="Path the log file")
parser.add_argument("-w", "--word", metavar="", type=str, help="What to look for, either string or regex")
parser.add_argument("-f", "--filemask", metavar="", type=str, help="Regex mask for filenames")
if len(sys.argv) == 1:  # No args passed
    sys.exit("No arguments passed, -h for help. Execution aborted.")
argsParsed = parser.parse_args()
try:
    txtMask = re.compile(argsParsed.filemask)
    regMask = re.compile(argsParsed.word)
    regex_valid = True
# re.I,re.M
#
except re.error:
    regex_valid = False
    sys.exit("Я не прикрутил поддержку плохого регекса, давайте заново.")
fPath = argsParsed.filepath

if os.path.isfile(fPath):  # If given path is a file
    with open(fPath) as file:
        lines = file.readlines()
    with open(r".\output.txt", "w") as outFile:  # Create output file
        print('Filename:{}'.format(fPath))
        for l in lines:
            for i in tqdm(range(100), desc='Progress', colour="#03A062"):
                if regMask.search(l):  # Looking for matches in every line
                    #  print("Found a match:  ", l)  # Print each match into console
                    outFile.write(l)  # Print each match into file
# re.search
elif os.path.isdir(fPath):
    #  txtMask = re.compile(r"(.*\.+log)|(.*\.+txt)", re.IGNORECASE)  # Filetypes to look for, e.g. (^.*\.+log$)|(^.*\.+txt$)
    dirFiles = os.listdir(fPath)  # All files in directory
    with open(r".\output.txt", "w") as outFile:
        #  for i in tqdm(range(100), desc='Progress', colour="#03A062"):
        #  for curFile in tqdm(dirFiles, desc='Progress'):  # Current file from the list
        for curFile in dirFiles:  # Current file from the list
            with open(os.path.join(fPath, curFile)) as cFile:  # Same as with single file, plus full path os.path.join(d, path)
                if txtMask.search(curFile):
                    outFile.write('\nFilename:{}\n'.format(curFile))
                    lines = cFile.readlines()
                    for l in tqdm(lines, desc='File {}'.format(curFile), colour="#03A062"):
                        if regMask.search(l):
                            outFile.write(l)
    print("\nDone!")
else:
    sys.exit("\nFiles/path not found. Execution aborted.")
