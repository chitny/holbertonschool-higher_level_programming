#!/usr/bin/python3
"""
Module: add_integer
adds 2 integers

"""


def add_integer(a, b=98):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an intenger")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an intenger")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        a = int(b)

    return a+b
