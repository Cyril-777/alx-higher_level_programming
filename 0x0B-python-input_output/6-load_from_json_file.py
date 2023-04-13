#!/usr/bin/python3
"""importing json"""
import json
"""a function that creates an Object from a JSON file"""


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
