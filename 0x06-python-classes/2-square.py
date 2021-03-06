#!/usr/bin/python3
'''Execute'''


class Square:
    '''Class providing all functions for
    creating a Square'''

    def __init__(self, size=0):
        '''Create a square'''

        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
