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

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @width.setter
    def width(self, value):
        """ Width setter """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """ Height setter """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value
