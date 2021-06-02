#!/usr/bin/python3
"""Name of the class"""


class Student:
    """Description of the class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        newdict = dict()
        if type(attrs) is list and all(type(i) is str for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    newdict.update({i: self.__dict__[i]})
            return newdict
        return self.__dict__.copy()
