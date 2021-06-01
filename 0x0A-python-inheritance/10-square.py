#!/usr/bin/python3
''' Executable command '''


Rectangle = __import__('7-base_geometry').Rectangle


class Square(Rectangle):
    ''' Square definition '''

    def __init__(self, size):
        ''' Initialization '''
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
