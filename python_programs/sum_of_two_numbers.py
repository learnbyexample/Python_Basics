#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    sys.exit("Error: Please provide exactly two numbers as arguments")
else:
    (num1, num2) = sys.argv[1:]
    total = int(num1) + int(num2)
    print("{} + {} = {}".format(num1, num2, total))
