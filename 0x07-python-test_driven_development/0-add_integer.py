#!/usr/bin/python3
"""Executable command

    You can test this function in
    /test/0-add_integer.txt
"""


def add_integer(a, b=98):
    """adds two integers or floats
        usage: add_integer(int, int) or add_integer(float, float)
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
