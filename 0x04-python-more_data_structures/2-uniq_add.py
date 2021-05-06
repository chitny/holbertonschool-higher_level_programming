#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(dict.fromkeys(my_list))
    x = 0
    for i in range(len(new_list)):
        x = x + new_list[i]
    return x
