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
        """ asd """
        return self.__width * self.__height

    def perimeter(self):
        """ asd """
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ asd """
        final_str = ""

        if (self.width == 0 or self.height == 0):
            return final_str
        for i in range(0, self.__height):
            final_str += ("#" * self.__width)
            if (i != self.__height - 1):
                final_str += '\n'

        return final_str

    @property
    def width(self):
        """ asd """
        return self.__width

    @property
    def height(self):
        """ asd """
        return self.__height

    @width.setter
    def width(self, value):
        """ asd """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """ asd """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value
