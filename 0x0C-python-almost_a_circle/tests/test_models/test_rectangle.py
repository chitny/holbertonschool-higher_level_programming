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
        b6 = Base(3)
        self.assertEqual(b6.id, 3)
        b7 = Base()
        self.assertEqual(b6.id, 4)
