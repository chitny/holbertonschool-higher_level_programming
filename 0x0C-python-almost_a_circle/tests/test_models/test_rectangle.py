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

    def test_5(self):
        """
        Test display method
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4)
        result1 = "##\n" \
            "##\n" \
            "##\n" \
            "##\n"
        r2 = Rectangle(2, 3)
        result2 = "##\n" \
            "##\n" \
            "##\n"
        r3 = Rectangle(1, 1)
        result3 = "#\n" \
                try:
            r1.display()
            self.assertEqual(sys.stdout.getvalue(), result1)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            r2.display()
            self.assertEqual(sys.stdout.getvalue(), result2)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            r3.display()
            self.assertEqual(sys.stdout.getvalue(), result3)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    if __name__ == '__main__':
        unittest.main()
