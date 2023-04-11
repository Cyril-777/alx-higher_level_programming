#!/usr/bin/python3
"""
a function that returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
    obj: Any Python object.
    a_class: A Python class.

    Returns:
    True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class;
    False otherwise.
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
