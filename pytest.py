import re
import argparse
from pathlib import Path
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("-f","--filepath", metavar="", type=Path, help="Path for log file")
parser.add_argument("-w","--word", metavar="", type=str, help="What to look for, either string or regex")
if len (sys.argv)==1:
    sys.exit("No arguments passed, -h for help. Execution aborted.")
argsParsed = parser.parse_args()
try:
    re.compile(argsParsed.word)
    regex_valid = True
# re.I re.M
# (^.*\.+log$)|(^.*\.+txt$)
except re.error:
    regex_valid = False
print (regex_valid)
if not argsParsed.filepath:
    sys.exit("Please provide filepath. Execution aborted.")
fPath=argsParsed.filepath
if os.path.isfile(fPath):
    foundFiles=1
    with open(fPath) as file:
        lines = file.readlines()
    for l in lines:
        print (l)
        
elif os.path.isdir(fPath):
    foundFiles=2
    dirFiles=os.listdir(fPath)
else:
    foundFiles=0
    print("Files/path not found\n")