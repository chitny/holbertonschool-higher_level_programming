#!/usr/bin/python3
"""Name of the class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Description of the class"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2
