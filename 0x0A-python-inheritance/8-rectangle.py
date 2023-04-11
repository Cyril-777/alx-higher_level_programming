#!/usr/bin/python3
"""
a class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """a Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with given width and height.

        Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
