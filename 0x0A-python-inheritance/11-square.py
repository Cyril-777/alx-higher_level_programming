#!/usr/bin/python3
"""
A module that contains a Square class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    square class that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with the given size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"calculates the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """should return, the square description: [Square] <width>/<height>"""
        return "[Square] {}/{}".format(self.__size, self.__size)
