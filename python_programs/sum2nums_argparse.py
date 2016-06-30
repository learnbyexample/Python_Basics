#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num1', type=int, help="first number")
parser.add_argument('num2', type=int, help="second number")
args = parser.parse_args()

total = args.num1 + args.num2
print("{} + {} = {}".format(args.num1, args.num2, total))
