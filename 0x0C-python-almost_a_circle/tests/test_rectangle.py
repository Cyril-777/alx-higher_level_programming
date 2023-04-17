#!/usr/bin/python3
"""
Unittest for Rectangle class
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 30)
        self.assertEqual(r1.y, 40)
        self.assertEqual(r1.id, 50)

    def test_width(self):
        r1 = Rectangle(10, 20)
        r1.width = 30
        self.assertEqual(r1.width, 30)

        with self.assertRaises(TypeError):
            r1.width = "hello"
        with self.assertRaises(ValueError):
            r1.width = -10

    def test_height(self):
        r1 = Rectangle(10, 20)
        r1.height = 30
        self.assertEqual(r1.height, 30)

        with self.assertRaises(TypeError):
            r1.height = "hello"
        with self.assertRaises(ValueError):
            r1.height = -10

    def test_x(self):
        r1 = Rectangle(10, 20)
        r1.x = 30
        self.assertEqual(r1.x, 30)

        with self.assertRaises(TypeError):
            r1.x = "hello"
        with self.assertRaises(ValueError):
            r1.x = -10

    def test_y(self):
        r1 = Rectangle(10, 20)
        r1.y = 30
        self.assertEqual(r1.y, 30)

        with self.assertRaises(TypeError):
            r1.y = "hello"
        with self.assertRaises(ValueError):
            r1.y = -10

    def test_area(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

        r1.width = 5
        r1.height = 10
        self.assertEqual(r1.area(), 50)

    def test_display(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.display(), None)

    def test_str(self):
        r1 = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(str(r1), "[Rectangle] (50) 30/40 - 10/20")

    def test_update(self):
        r1 = Rectangle(10, 20, 30, 40, 50)
        r1.update(60, 20, 30, 40, 50)
        self.assertEqual(str(r1), "[Rectangle] (60) 40/50 - 20/30")

        r1.update(id=70, y=60, x=50)
        self.assertEqual(str(r1), "[Rectangle] (70) 50/60 - 20/30")

    def test_to_dictionary(self):
        r1 = Rectangle(10, 20, 30, 40, 50)
        d = r1.to_dictionary()
        self.assertEqual(d, {"id": 50, "width": 10, "height": 20, "x": 30, "y": 40})

if __name__ == "__main__":
    unittest.main()