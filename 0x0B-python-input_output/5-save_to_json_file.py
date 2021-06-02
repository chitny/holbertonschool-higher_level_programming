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
    with open(filename, mode="w+") as myfile:
        json.dumps(my_obj, myfile)
