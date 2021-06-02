#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo

"""


def append_after(filename="", search_string="", new_string=""):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """

    with open(filename, "r") as myfile:
        text = myfile.readlines()

    with open(filename, "w") as myfile2:
        st = ""
        for line in text:
            st = st + line
            if search_string in line:
                st += new_string
        myfile2.write(st)
