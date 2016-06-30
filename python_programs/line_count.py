#!/usr/bin/python3

import sys, pathlib, subprocess, re

if len(sys.argv) != 2:
    sys.exit("Error: Please provide exactly one filename as argument")

program_name = sys.argv[0]
filename = sys.argv[1]

if not pathlib.Path(filename).is_file():
    sys.exit("File '{}' not found".format(filename))

if re.search(r'line_count.py', program_name):
    lc = subprocess.getoutput('wc -l < ' + filename)
    print("No. of lines in '{}' is: {}".format(filename, lc))
elif re.search(r'word_count.py', program_name):
    wc = subprocess.getoutput('wc -w < ' + filename)
    print("No. of words in '{}' is: {}".format(filename, wc))
else:
    sys.exit("Program name '{}' not recognized".format(program_name))
