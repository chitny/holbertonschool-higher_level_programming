#!/usr/bin/python3
def roman_to_int(roman_string):

    rom = {'I': 1, 'V': 5, 'X': 10,
           'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    if type(roman_string) is not str or roman_string is None:
        return 0

    if len(roman_string) == 1:
        return rom.get(roman_string)

    for i in range(len(roman_string)):
        if i + 1 == len(roman_string):
            x = roman_string[i]
            z = rom.get(x)
            result = result + z
        elif rom.get(roman_string[i]) >= rom.get(roman_string[i + 1]):
            x = roman_string[i]
            z = rom.get(x)
            result = result + z
        else:
            x = roman_string[i]
            z = rom.get(x)
            result = result - z
    return result
