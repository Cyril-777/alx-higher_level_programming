#!/usr/bin/python3
"""Unittest for max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class myfirsteverunittestsclassimsoexcitedomg(unittest.TestCase):
    def test_empty(self):
        self.assertIsNone(max_integer())

    def test_positive_nums(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_nums(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_nums(self):
        self.assertEqual(max_integer([-1, 0, 1, -2]), 1)

    def test_same_nums(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_single_num(self):
        self.assertEqual(max_integer([3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.0, 2.5, 3.7]), 3.7)

    def test_strings(self):
        self.assertRaises(TypeError, max_integer, ["alx", "school"])

    def test_boolean(self):
        self.assertEqual(max_integer([True, False, True]), True)

    def test_none(self):
        self.assertRaises(TypeError, max_integer, [None])

if __name__ == '__main__':
    unittest.main()
