#!/usr/bin/python3
''' Executable command '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Defines a rectangle '''

    __width = 0
    __heigth = 0

    def __init__(self, width, height):
        ''' The init method '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        ''' Calculate the area '''
        return self.__width * self.__height

    def __str__(self):
        ''' String returned on printing '''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
