#!/usr/bin/python3
"""
 returns True if the object is exactly an instance of
 the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    Check if an object is of a specified class.

    Args:
    obj: Any Python object.
    a_class: A Python class.

    Returns:
    True if obj is of type a_class, False otherwise.
    """
    if (type(obj) == a_class):
        return (True)
    return (False)
