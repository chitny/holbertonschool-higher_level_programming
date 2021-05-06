#!/usr/bin/python3
def roman_to_int(roman_string):

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    result = 0

    if type(roman_string) is not str or roman_string is None:
        return 0

    if len(roman_string) == 1:
        return roman_dict.get(roman_string)

    for i in range(len(roman_string)):
        if i + 1 == len(roman_string):
            result += roman_dict. get(roman_string[i])
        elif roman_dict.get(roman_string[i]) >= roman_dict.get(roman_string[i + 1]):
            result += roman_dict. get(roman_string[i])
        else:
            result -= roman_dict. get(roman_string[i])
    return result
