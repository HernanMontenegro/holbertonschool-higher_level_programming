#!/usr/bin/python3
"""Executable command

    You can test this function in
    /test/3-say_my_name.txt
"""


def print_square(size):
    if ((type(size) == float and size < 0) or (type(size) != int)):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        print("#" * size)
