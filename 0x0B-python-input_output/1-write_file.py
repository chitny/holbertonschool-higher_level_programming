#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo

"""


def write_file(filename="", text=""):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """
    with open(filename, mode="w+", encoding="utf-8") as myfile:
        return myfile.write(text)
