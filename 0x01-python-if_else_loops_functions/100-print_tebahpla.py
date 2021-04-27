#!/usr/bin/python3
for x in range(122, 96, -1):
    if x % 2 == 0:
        x= chr(x)
    else:
        x=chr(x).upper()
    print("{}".format(x), end="")
