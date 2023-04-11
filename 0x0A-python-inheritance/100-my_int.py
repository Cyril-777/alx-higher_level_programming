#!/usr/bin/env python3
"""
rebel class MyInt that inherits from int
and inverts operations!
"""


class MyInt(int):
    """
    A subclass of the built-in int class that overrides the ==
    and != operators.
    """

    def __eq__(self, value):
        """
        Overrides the == operator.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Overrides the != operator.
        """
        return self.real == value
