#!/usr/bin/python3
"""Name of the class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Description of the class"""

    def __init__(self, width, height):
        """never forget description"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area():
        """never forget description"""
        return self.__width * self.__height

    def __str__(self):
        """never forget description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
