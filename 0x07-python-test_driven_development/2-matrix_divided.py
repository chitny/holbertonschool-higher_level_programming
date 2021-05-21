#!/usr/bin/python3
"""
Module: matrix_divided
Divides all elements of a matrix

"""


from typing import Type


def matrix_divided(matrix, div)::
    """descripcion de la funcion,
    lo que hace y para que sirve
    """
    for i in matrix[]:

    if matrix[0][0] != matrix[0][1]:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return new_matrix


matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix(list of lists) of integers/floats
All elements of the matrix should be divided by div, rounded to 2 decimal places
