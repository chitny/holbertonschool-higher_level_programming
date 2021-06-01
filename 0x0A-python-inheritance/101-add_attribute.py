#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo

"""


def add_attribute(obj, attr, value):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
