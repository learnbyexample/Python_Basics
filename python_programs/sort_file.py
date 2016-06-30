#!/usr/bin/python3

import argparse, subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="file to be sorted", required=True)
parser.add_argument('-u', help="sort uniquely", action="store_true")
args = parser.parse_args()

if args.u:
    subprocess.call(['sort', '-u', args.file, '-o', args.file])
else:
    subprocess.call(['sort', args.file, '-o', args.file])
