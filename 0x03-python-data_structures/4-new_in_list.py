#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    largo = len(my_list)
    if idx in range(largo):
        new_list[idx] = element
        return new_list
    else:
        return my_list
