#!/usr/bin/python3
""" class Student """


import json
import os.path
import sys


def save_to_json_file(my_obj, filename):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """
    with open(filename, mode="w+") as myfile:
        json.dump(my_obj, myfile)


def load_from_json_file(filename):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """
    with open(filename, mode="r", encoding="utf-8") as myfile:
        return (json.load(myfile))


if (os.path.isfile("add_item.json")):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, "add_item.json")
