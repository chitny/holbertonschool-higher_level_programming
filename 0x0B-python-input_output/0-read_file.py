#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo
"""


def read_file(filename=""):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """

    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
