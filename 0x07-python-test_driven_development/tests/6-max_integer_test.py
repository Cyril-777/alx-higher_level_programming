#!/usr/bin/python3
"""Unittest for max_integer function
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class myfirsteverunittestsclassimsoexcitedomg(unittest.TestCase):
    def test_empty(self):
        """Test the function when an empty list is passed as input.

        Expected behavior: The function should return None.
        """
        self.assertIsNone(max_integer())

    def test_positive_nums(self):
        """Test the function when a
        list of positive integers is passed as input.

        Expected behavior: The function should
        return the maximum integer in the list.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_nums(self):
        """Test the function when a list of
        negative integers is passed as input.

        Expected behavior: The function should return
        the maximum integer in the list.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_nums(self):
        """Test the function when a
        list of mixed positive and
        negative integers is passed as input.

        Expected behavior: The function should return
        the maximum integer in the list.
        """
        self.assertEqual(max_integer([-1, 0, 1, -2]), 1)

    def test_same_nums(self):
        """Test the function when a list
        of the same integers is passed as input.

        Expected behavior: The function should return
        the same integer.
        """
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_single_num(self):
        """Test the function when a list with a single
        integer is passed as input.

        Expected behavior: The function should return
        the same integer.
        """
        self.assertEqual(max_integer([3]), 3)

    def test_floats(self):
        """Test the function when a list of
        floats is passed as input.

        Expected behavior: The function should return
        the maximum float in the list.
        """
        self.assertEqual(max_integer([1.0, 2.5, 3.7]), 3.7)

    def test_strings(self):
        """Test the function when a list of strings is passed
        as input.

        Expected behavior: The function should raise a TypeError.
        """
        self.assertRaises(TypeError, max_integer, ["alx", "school"])

    def test_boolean(self):
        """Test the function when a list of booleans is passed as input.

        Expected behavior: The function should return the maximum
        boolean in the list.
        """
        self.assertEqual(max_integer([True, False, True]), True)

    def test_none(self):
        """Test the function when a list
        containing None is passed as input.

        Expected behavior: The function should raise a TypeError.
        """
        self.assertRaises(TypeError, max_integer, [None])


if __name__ == '__main__':
    unittest.main()
