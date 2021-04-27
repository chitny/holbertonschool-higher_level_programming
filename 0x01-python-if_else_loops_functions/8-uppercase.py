#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <=122:
            result += chr(ord(ch)-32)
        else:
            result += chr(ord(ch))
    print(result)
