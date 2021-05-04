#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    num = len(my_list)
    for i in my_list:
        num = num-1
        print("{:d}".format(my_list[num]))
