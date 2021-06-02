#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo
"""


def pascal_triangle(n):
    """descripcion de la funcion,
    lo que hace y para que sirve
    """
    newlist = []
    actlist = [1]

    if n <= 0:
        return []

    for i in range(0, n):

        if i == 0:
            newlist.append([1])
        else:
            tmplist = []

            for j in range(0, i+1):
                add1 = 0

                if j > 0:
                    add1 = actlist[j-1]

                add2 = 0

                if j < len(actlist):
                    add2 = actlist[j]

                tmplist.append(add1+add2)
            actlist = tmplist
            newlist.append(actlist)
    return (newlist)
