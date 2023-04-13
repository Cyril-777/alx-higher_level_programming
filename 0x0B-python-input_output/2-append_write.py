#!/usr/bin/python3
"""
 a function that appends a string at the end of a text file
 (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 text file
    and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        c = f.write(text)
    return c
