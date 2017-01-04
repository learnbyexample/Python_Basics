#!/usr/bin/python3

import fileinput

with fileinput.input(inplace=True) as f:
    for line in f:
        line = line.replace('line of text', 'line')
        print(line, end='')
