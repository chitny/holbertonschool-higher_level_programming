#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nuevo_d = {}
    for i in a_dictionary:
        nuevo_d[i] = a_dictionary[i]*2
    return nuevo_d
