#!/usr/bin/python3
"""
a function that returns True if the object is an instance of class
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """
    return (type(obj) != a_class and isinstance(obj, a_class))
