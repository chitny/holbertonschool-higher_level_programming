#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)-1
    sum = 0
    for x in range(args):
        sum = sum+(int(sys.argv[x+1]))
    print("{}".format(sum))
