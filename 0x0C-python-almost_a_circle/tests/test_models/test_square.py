#!/usr/bin/python3
"""Unittest square.
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_10(self):
        """Test Square class: check for attributes."""

        s0 = Square(8)
        self.assertEqual(s0.id, 8)
        s1 = Square(8, 1, 4)
        self.assertEqual(s1.height, 8)
        self.assertEqual(s1.width, 8)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 8)

        s1 = Square(9, 8, 7, 6)
        self.assertEqual(str(s1), "[Square] (6) 8/7 - 9")

        s1 = Square(8)
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

        with self.assertRaises(TypeError) as x:
            s1 = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'", str(
                x.exception))

        s1 = Square(10)
        self.assertEqual(s1.area(), 100)
        s2 = Square(4, 1, 2, 5)
        s2.update(28)
        self.assertEqual(s2.id, 28)
        f = io.StringIO()
        s3 = Square(7)
        with contextlib.redirect_stdout(f):
            s3.display()
        s = f.getvalue()
        res = "#######\n#######\n#######\n#######\n"
        self.assertEqual(s, res)

    def test_11(self):
        """Test Square class: check for size attribute."""

        s1 = Square(8)
        self.assertEqual(s1.size, 8)
        s2 = Square(9, 8, 7, 6)
        self.assertEqual(s2.size, 9)

        with self.assertRaises(TypeError) as x:
            s = Square("Holberton", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(2, "School")
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(1, 2, "three", 4)
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(0, 8)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(-1)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, -3)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, 5, -5, 6)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_12(self):
        """Test update method on Square."""

        s1 = Square(5)
        s1.update(18)
        self.assertEqual(s1.id, 18)
        s1.update(x=22)
        self.assertEqual(s1.x, 22)
        s1.update(size=8, id=88, y=1)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.id, 88)
        self.assertEqual(s1.y, 1)
        s1.update()
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.id, 88)
        self.assertEqual(s1.y, 1)

        s1 = Square(9)
        with self.assertRaises(TypeError) as x:
            s1.update(1, 2, 3, "hello")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s1.update("hello", 4, 5)
        self.assertEqual("id must be an integer", str(x.exception))

    def test_14(self):
        """Test for public method to_dictionary."""

        s1 = Square(88, 1, 2)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 1, 'y': 2, 'id': 1, 'size': 88}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(len(s1_dictionary), len(s2_dictionary))
        self.assertEqual(type(s2_dictionary), dict)
        self.assertFalse(s1 == s2)

        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            s1 = Square(10, 2, 1, 9)
            s1_dictionary = s1.to_dictionary("Holberton")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
