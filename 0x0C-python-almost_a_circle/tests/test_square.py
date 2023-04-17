#!/usr/bin/python3
"""
Unit tests for Square class.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Class containing test cases for Square.
    """
    def setUp(self):
        """
        Method to create a Square instance to be used for testing.
        """
        self.s = Square(5)

    def test_attributes(self):
        """
        Test that the Square instance has the correct attributes.
        """
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'size'))
        self.assertTrue(hasattr(self.s, 'x'))
        self.assertTrue(hasattr(self.s, 'y'))

    def test_methods(self):
        """
        Test that the Square instance has the correct methods.
        """
        self.assertTrue(hasattr(self.s, 'area'))
        self.assertTrue(hasattr(self.s, 'display'))
        self.assertTrue(hasattr(self.s, '__str__'))
        self.assertTrue(hasattr(self.s, 'update'))
        self.assertTrue(hasattr(self.s, 'to_dictionary'))

    def test_inheritance(self):
        """
        Test that Square inherits from Rectangle.
        """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_size_getter(self):
        """
        Test that the size getter returns the correct value.
        """
        self.assertEqual(self.s.size, 5)

    def test_size_setter(self):
        """
        Test that the size setter sets the correct value.
        """
        self.s.size = 10
        self.assertEqual(self.s.size, 10)
        self.assertEqual(self.s.width, 10)
        self.assertEqual(self.s.height, 10)

    def test_str(self):
        """
        Test that the __str__ method returns the correct string.
        """
        self.assertEqual(str(self.s), '[Square] ({}) 0/0 - 5'.format(self.s.id))

    def test_update(self):
        """
        Test that the update method updates the correct attributes.
        """
        self.s.update(10, 5, 1, 2)
        self.assertEqual(self.s.id, 10)
        self.assertEqual(self.s.size, 5)
        self.assertEqual(self.s.x, 1)
        self.assertEqual(self.s.y, 2)

    def test_to_dictionary(self):
        """
        Test that the to_dictionary method returns the correct dictionary.
        """
        d = self.s.to_dictionary()
        self.assertTrue(isinstance(d, dict))
        expected = {'id': self.s.id, 'size': 5, 'x': 0, 'y': 0}
        self.assertDictEqual(d, expected)

if __name__ == "__main__":
    unittest.main()