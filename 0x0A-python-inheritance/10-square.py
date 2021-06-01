#!/usr/bin/python3
''' Executable command '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Defines a rectangle '''

    __width = 0
    __heigth = 0

    def __init__(self, width, height):
        ''' The init method '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        ''' Calculate the area '''
        return self.__width * self.__height

    def __str__(self):
        ''' String returned on printing '''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    ''' Square definition '''

    __size = 0

    def __init__(self, size):
        ''' Initialization '''
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
