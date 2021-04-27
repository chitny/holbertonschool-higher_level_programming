#!/usr/bin/python3
def remove_char_at(str, n):
    ch = len(str)
    for x in range (0, ch):
        if x != n:
            print(str[x], end="")