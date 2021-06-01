#!/usr/bin/python3
"""Name of the class"""


class MyInt(int):
    """Description of the class"""

    def __eq__(self, x):
        return super().__ne__(x)

    def __ne__(self, x):
        return super().__eq__(x)
