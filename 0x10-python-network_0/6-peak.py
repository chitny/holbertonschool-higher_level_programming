#!/usr/bin/python3
"""Find a peak"""


def find_peak(intlist):
    """Finds a peak function"""

    if intlist is None or intlist == []:
        return None
    largo = len(intlist)
    medio = ((largo) // 2)
    medio = int(medio)
    if largo == 1:
        return intlist[0]
    if largo == 2:
        return max(intlist)
    if intlist[medio] >= intlist[medio - 1] and\
            intlist[medio] >= intlist[medio + 1]:
        return intlist[medio]
    if medio > 0 and intlist[medio] < intlist[medio + 1]:
        return find_peak(intlist[medio:])
    if medio > 0 and intlist[medio] < intlist[medio - 1]:
        return find_peak(intlist[:medio])
