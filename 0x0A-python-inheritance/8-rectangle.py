#!/usr/bin/python3
''' Executable command '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Defines a rectangle '''

    def __init__(self, width, height):
        ''' The init method '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
