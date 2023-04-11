#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Function that checks if an object is an instance of,
    or inherited from, a specified class.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class that the object may or may not belong to.

    Returns:
        bool: True if the object is an instance of,
        or inherited from, the specified class. False otherwise.
    """
    return isinstance(obj, a_class)
