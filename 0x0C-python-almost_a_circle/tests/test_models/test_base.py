#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_id(self):
        """Test id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Test to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(type(json_string), str)
        self.assertCountEqual(json.loads(json_string), [dictionary])

    def test_from_json_string(self):
        """Test from_json_string method"""
        json_string = '[{"id": 89, "width": 10, "height": 4, "x": 7, "y": 8}]'
        list_input = Base.from_json_string(json_string)
        self.assertEqual(type(list_input), list)
        self.assertEqual(len(list_input), 1)
        self.assertEqual(type(list_input[0]), dict)
        self.assertEqual(list_input[0], {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8})

    def test_create(self):
        """Test create method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1.__str__(), r2.__str__())

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual([r1.to_dictionary(), r2.to_dictionary()], json.load(file))

    def test_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles), 2)
        self.assertEqual(list_rectangles[0].__str__(), r1.__str__())
        self.assertEqual(list_rectangles[1].__str__(), r2.__str__())

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "id,width,height,x,y\n1,10,7,2,8\n2,2,4,0,0\n")

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rectangles), 2)
        self.assertEqual(list_rectangles[0].__str__(), r1.__str__())
        self.assertEqual(list_rectangles[1].__str__(), r2.__str__())

    def test_save_to_file_csv_None(self):
        """Test save_to_file_csv method when list_rectangles is None"""
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "")

    def test_save_to_file_csv_empty_list(self):
        """Test save_to_file_csv method when list_rectangles is an empty list"""
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "")

    def test_load_from_file_csv_None(self):
        """Test load_from_file_csv method when file does not exist"""
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        list_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles, [])

    def test_load_from_file_csv_empty_file(self):
        """Test load_from_file_csv method when file is empty"""
        open("Rectangle.csv", "w").close()
        list_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles, [])


if __name__ == "__main__":
    unittest.main()