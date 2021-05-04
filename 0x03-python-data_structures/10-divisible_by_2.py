#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
     for i in len(my_list):
          divis = my_list[i] % 10
           if divis == 0 or divis == 2 or divis == 4 or divis == 6 or divis == 8:
                new_list[i] = "True"
            else:
                new_list[i] = "False"
    return new_list
