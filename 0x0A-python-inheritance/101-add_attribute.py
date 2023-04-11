#!/usr/bin/python3
"""function that adds a new attribute to an object if it is possible"""


def add_attribute(object, attribute, value):
    """
    Add a new attribute to an object if possible.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
