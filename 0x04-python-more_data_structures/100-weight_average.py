#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    divi = 0
    for tup in my_list:
        average = average + tup[0] + tup[1]
        divi = diiv + tup[1]
    return float(average/divi)
