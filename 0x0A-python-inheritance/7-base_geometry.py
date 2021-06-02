#!/usr/bin/python3
"""Name of the class"""


class BaseGeometry:
    """Description of the class"""

    def area(self):
        """dont forget description"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """dont forget description"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
