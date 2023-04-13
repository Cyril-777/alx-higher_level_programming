#!/usr/bin/python3
"""importing json"""
import json
"""a function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.
    """
    return json.dumps(my_obj)
