#!/usr/bin/python3
"""Unittest base.
Test cases for Base class.
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1(self):
        """create an instance and check id."""

        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(24)
        self.assertEqual(b2.id, 24)
        b3 = Base(1024)
        self.assertEqual(b3.id, 1024)
        b4 = Base(0)
        self.assertEqual(b4.id, 0)
        b5 = Base(-10)
        self.assertEqual(b5.id, -10)
        b6 = Base(4)
        self.assertEqual(b6.id, 4)
        b7 = Base()
        self.assertEqual(b7.id, 3)


        b7 = Base()
        self.assertEqual(type(b7), Base)
        self.assertTrue(isinstance(b7, Base))

    def test_15(self):
        """Test static method to_json_string with regular dict."""

        d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_d = Base.to_json_string([d])
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(isinstance(json_d, str))
        self.assertCountEqual(
            json_d, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        json_d_1 = Base.to_json_string([])
        self.assertEqual(json_d_1, "[]")
        json_d_2 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")


       
        s1 = ("to_json_string() missing 1 required positional argument: " +
              "'list_dictionaries'")
        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(s1, str(x.exception))
        s2 = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(s2, str(x.exception))

    def test_16(self):
        """Test class method save_to_file with normal types."""

        r0 = Rectangle(10, 7, 2, 8)
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file([r0, r1])
        res = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
        Rectangle.save_to_file(None)
        res = "[]"
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)
        s0 = Square(9, 3, 1, 12)
        s1 = Square(6, 7)
        Square.save_to_file([s0, s1])
        res = ('[{"id": 12, "size": 9, "x": 3, "y": 1},' +
               ' {"id": 3, "size": 6, "x": 7, "y": 0}]')
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
        Square.save_to_file(None)
        res = "[]"
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)


        with self.assertRaises(AttributeError) as x:
            Base.save_to_file([Base(9), Base(5)])
        self.assertEqual(
            "'Base' object has no attribute 'to_dictionary'", str(
                x.exception))
        with self.assertRaises(AttributeError) as x:
            Rectangle.save_to_file([3, 4])
        self.assertEqual(
            "'int' object has no attribute 'to_dictionary'", str(
                x.exception))
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file(5)
        self.assertEqual(
            "'int' object is not iterable", str(
                x.exception))


        s1 = ("save_to_file() missing 1 required" +
              " positional argument: 'list_objs'")
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file()
        self.assertEqual(s1, str(x.exception))
        s2 = ("save_to_file() takes 2 positional" +
              " arguments but 3 were given")
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file([Rectangle(9, 4), Rectangle(8, 9)], 98)
        self.assertEqual(s2, str(x.exception))

    def test_17(self):
        """Test static method from_json_string with normal types."""

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        res = [{'width': 10, 'height': 4, 'id': 89},
               {'width': 1, 'height': 7, 'id': 7}]
        self.assertCountEqual(list_output, res)
        self.assertEqual(type(list_output), list)

        s1 = ("from_json_string() missing 1" +
              " required positional argument: 'json_string'")
        with self.assertRaises(TypeError) as x:
            Rectangle.from_json_string()
        self.assertEqual(s1, str(x.exception))
        s2 = "from_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            Rectangle.from_json_string("Hi", 98)
        self.assertEqual(s2, str(x.exception))

    def test_18(self):
        """Test class method create with normal types."""

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)


        with self.assertRaises(TypeError) as x:
            r1 = "Hello"
            r2 = Rectangle.create(r1)
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_19(self):
        """Test class method load_from_file with normal types."""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for x in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(x[0]), str(x[1]))

        s1 = Square(10, 2)
        s2 = Square(9)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for x in zip(list_squares_input, list_squares_output):
            self.assertEqual(str(x[0]), str(x[1]))


        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])


        s = "load_from_file() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            list_rectangles_output = Rectangle.load_from_file("Hello")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
