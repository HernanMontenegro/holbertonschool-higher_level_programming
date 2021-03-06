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
        self.width = width
        self.height = height
        return

    def area(self):
        """ asd """
        return self.__width * self.__height

    def perimeter(self):
        """ asd """
        if (self.height == 0 or self.width == 0):
            return 0
        return (self.__height * 2) + (self.__width * 2)

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
