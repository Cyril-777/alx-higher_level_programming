#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ A class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class.
        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        else:
            return 2 * (self._width + self._height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            recstr: A string representation of the rectangle.
        """

        recstr = ""

        if self.width == 0 or self.height == 0:
            return recstr

        for i in range(self.height):
            recstr += ("#" * self.width) + "\n"

        return recstr[:-1]
