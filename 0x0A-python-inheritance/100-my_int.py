#!/usr/bin/python3
"""
rebel class MyInt that inherits from int
and inverts operations!
"""


class MyInt(int):
    """
    A subclass of the built-in int class that overrides the ==
    and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator.
        """
        return super().__eq__(other)
