#!/usr/bin/python3
"""Unittest rectangle
Test cases for the Rectangle class.
Each test has the number of the task,
and the number of the test for that task
(i.e 'test_17_0' for the first test of task 17)
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_2(self):
        """Check for attributes values."""

        r1 = Rectangle(20, 4)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(20, 4, 4, 5, 24)
        self.assertEqual(r2.width, 20)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)

        with self.assertRaises(TypeError) as x:
            r0 = Rectangle(7)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'", str(
                x.exception))
        s = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle()
        self.assertEqual(s, str(x.exception))

        r1 = Rectangle(12, 16)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_3(self):
        """Check for wrong attributes."""

        with self.assertRaises(TypeError) as x:
            r = Rectangle("Holberton", 8)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(8, "el pepocho")
        self.assertEqual("height must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, "three", 4)
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, 3, "four")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 8)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(8, 0)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(8, -8)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(8, 8, -8, 8)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(8, 8, 8, -8)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_4(self):
        """Test for area with normal types."""

        r1 = Rectangle(8, 2)
        self.assertEqual(r1.area(), 16)
        r2 = Rectangle(75, 2)
        self.assertEqual(r2.area(), 150)
        r3 = Rectangle(8, 10, 0, 0, 12)
        self.assertEqual(r3.area(), 80)

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(3, 2)
            r1.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_5(self):
        """Test for public method display."""

        f = io.StringIO()
        r1 = Rectangle(6, 5)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "######\n######\n######\n######\n######\n"
        self.assertEqual(s, res)

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(88, 8)
            r1.display(88)
        self.assertEqual(
            "display() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_6(self):
        """Test for __str__ representation."""

        f = io.StringIO()
        r1 = Rectangle(8, 8, 8, 8, 8)
        with contextlib.redirect_stdout(f):
            print(r1)
        s = f.getvalue()
        res = "[Rectangle] (8) 8/8 - 8/8\n"
        self.assertEqual(s, res)

    def test_7(self):
        """Test for public method display with x and y."""

        f = io.StringIO()
        r1 = Rectangle(8, 3, 2, 2)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "\n\n  ########\n  ########\n  ########\n"
        self.assertEqual(s, res)

    def test_8(self):
        """Test for public method update."""

        r1 = Rectangle(80, 80, 80, 80)
        r1.update(88)
        self.assertEqual(r1.id, 88)
        r1.update(88, 2)
        self.assertEqual(r1.width, 2)
        r1.update(88, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(88, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(88, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (88) 4/5 - 2/3")

        r1 = Rectangle(10, 20, 30, 40)
        with self.assertRaises(TypeError) as x:
            r1.update("holberton")
        self.assertEqual("id must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r1.update(77, 88, "school")
        self.assertEqual("height must be an integer", str(x.exception))

    def test_9(self):
        """Test for public method update with kwargs."""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)

        r1 = Rectangle(10, 20, 30, 40)
        with self.assertRaises(TypeError) as x:
            r1.update(id='holberton')
        self.assertEqual("id must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r1.update(height=88, x=8, width="school")
        self.assertEqual("width must be an integer", str(x.exception))

    def test_13(self):
        """Test for public method to_dictionary."""

        r1 = Rectangle(18, 7, 8, 9)
        r1_dictionary = r1.to_dictionary()
        r_dictionary = {'x': 8, 'y': 9, 'id': 1, 'height': 7, 'width': 17}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(r1 == r2)

        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(10, 2, 1, 9)
            r1_dictionary = r1.to_dictionary("Holberton")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
