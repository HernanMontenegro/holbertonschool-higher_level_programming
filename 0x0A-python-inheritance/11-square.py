#!/usr/bin/python3
''' Executable command '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Square definition '''

    def __init__(self, size):
        ''' Initialization '''
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        ''' What should print '''
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
