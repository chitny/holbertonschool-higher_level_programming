#!/usr/bin/python3
def remove_char_at(str, n):
    ch = len(str)
    ch2 = ""
    for x in range(0, ch):
        if x != n:
            ch2 = ch2+str[x]
    return ch2
