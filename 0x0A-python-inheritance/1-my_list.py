#!/usr/bin/python3
"""
prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    A subclass of the built-in list class
    that includes a method for printing the list
    in sorted order.

    Public methods:
    print_sorted() -- prints the list in ascending order
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Returns:
        None
        """
        sorted_list = sorted(self)
        print(sorted_list)
