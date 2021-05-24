#!/usr/bin/python3
"""
Executable command
"""


class Rectangle:
    """ Class that defines a
    rectangle
    """

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """ Called when a new instance is created """

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        final_str = ""

        for i in range(0, self.__height):
            final_str += ("#" * self.__width) + '\n'

        return final_str

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value
