#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    largo = len(my_list)
    if idx in range(largo):
        return my_list[idx]
    else:
        my_list[idx] = element
        return my_list
