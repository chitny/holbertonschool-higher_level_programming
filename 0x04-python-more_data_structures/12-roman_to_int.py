#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    if len(roman_string) == 1:
        return roman_dict.get(roman_string)
    else:
        for i in range(len(roman_string)):
            if i + 1 == len(roman_string):
                x = roman_string[i]
                z = roman_dict.get(x)
                result = result + z
            elif roman_dict.get(roman_string[i]) >= roman_dict.get(roman_string[i + 1]):
                x = roman_string[i]
                z = roman_dict.get(x)
                result = result + z
            else:
                x = roman_string[i]
                z = roman_dict.get(x)
                result = result - z
    return result
