#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    largo = len(my_list)
    if idx in range(largo):
        del my_list[idx]
        return my_list
    else:
        return my_list
