#!/usr/bin/python3
"""Class Square."""


class Square():
    """Represents an square."""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        areas = self.__size * self.__size
        return areas

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
