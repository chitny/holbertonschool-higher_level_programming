#!/usr/bin/python3
"""Class named Base"""

import json
import os


class Base:
    """This class will be the “base” of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            tosave = "[]"
        else:
            tosave = cls.to_json_string([i.to_dictionary() for i in list_objs])

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(tosave)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        insta = cls(82, 90)
        insta.update(**dictionary)
        return insta

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        list_inst = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for i in cls.from_json_string(file.read()):
                    list_inst.append(cls.create(**i))

        return list_inst
