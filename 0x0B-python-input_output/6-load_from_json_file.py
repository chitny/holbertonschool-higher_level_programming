#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo

"""
import json


def load_from_json_file(filename):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """
    with open(filename, mode="r", encoding="utf-8") as myfile:
        return (json.load(myfile))
