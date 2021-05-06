#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    valor = 0
    for i, j, in a_dictionary.items():
        if j > valor:
            valor = j
            nombre = i
    return nombre
