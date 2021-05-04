#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in len(my_list):
        divis = my_list[i] % 10
        if divis == 0 or divis == 2 or divis == 4 or divis == 6 or divis == 8:
            return True
        else:
            return False
