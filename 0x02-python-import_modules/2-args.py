#!/usr/bin/python3
import sys
args = sys.argv[1:]
n = len(args)
if n == 0:
    print("Number of argument(s).")
elif n == 1:
    print("Number of argument:")
else:
    print("Number of arguments:")
if n > 0:
    print()
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
