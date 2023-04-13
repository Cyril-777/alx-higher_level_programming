#!/usr/bin/python3
"""importing json"""
import json
"""a function that returns an object (Python data structure)
represented by a JSON string"""


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.
    """
    return json.loads(my_str)
