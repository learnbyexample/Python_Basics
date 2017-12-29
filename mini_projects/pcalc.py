#!/usr/bin/python3

"""
eval is used, so use at your own risk

Examples:
$ ./pcalc.py -vx '0b101 + 3'
0b101 + 3 = 0x8
$ ./pcalc.py '0x23'
35
$ ./pcalc.py -f2 '76/13'
5.85
$ ./pcalc.py '27**12'
150094635296999121
$ echo '97 + 232' | ./pcalc.py
329

$ ./pcalc.py '42 + 2s'
Error: Not a valid input expression
"""

import argparse, sys, fileinput

parser = argparse.ArgumentParser()
parser.add_argument('arith_expr', nargs='?', default=sys.stdin, help="arithmetic expression")
parser.add_argument('-v', help="verbose, show both input and output in result", action="store_true")
parser.add_argument('-f', type=int, help="specify floating point output precision")
parser.add_argument('-b', help="output in binary format", action="store_true")
parser.add_argument('-o', help="output in octal format", action="store_true")
parser.add_argument('-x', help="output in hexadecimal format", action="store_true")
args = parser.parse_args()

if type(args.arith_expr) != str:
    args.arith_expr = fileinput.input().readline().strip()
ip_expr = args.arith_expr

try:
    result = eval(ip_expr)

    if args.f:
        result = "{0:.{1}f}".format(result, args.f)
    elif args.b:
        result = "{:#b}".format(int(result))
    elif args.o:
        result = "{:#o}".format(int(result))
    elif args.x:
        result = "{:#x}".format(int(result))

    if args.v:
        print("{} = {}".format(args.arith_expr, result))
    else:
        print(result)
except (NameError, SyntaxError) as e:
    sys.exit("Error: Not a valid input expression")

