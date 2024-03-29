#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its contents to stdout.
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
