#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo

"""


def inherits_from(obj, a_class):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
