#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo

"""

import json


def save_to_json_file(my_obj, filename):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """
    with open(filename, mode="w+", encoding="utf-8") as myfile:
        json.dump(my_obj, myfile)
    return
