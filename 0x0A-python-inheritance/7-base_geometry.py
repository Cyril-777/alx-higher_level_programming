#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """
    A class representing a basic geometric shape.
    """
    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is an integer greater than 0.

        Args:
        name: A string representing the name of the value being validated.
        value: An integer representing the value being validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
