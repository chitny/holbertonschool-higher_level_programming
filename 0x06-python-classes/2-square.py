#!/usr/bin/python3
"""Class Square."""


class Square():
    """Represents an square."""

    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
