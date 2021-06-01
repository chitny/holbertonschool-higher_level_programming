#!/usr/bin/python3
"""Class MyList"""


class MyList(list):
    """Description of the class"""

    def print_sorted(self):

        newlist = self[:]
        newlist.sort()
        print("{}".format(newlist))
