#!/usr/bin/python3
'''Execute'''


class Square:
    '''Class providing all functions for
    creating a Square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Create a square'''

        self.__size = 0
        self.__position = (0, 0)

        self.position = position
        self.size = size

    def area(self):
        return self.__size**2

    def my_print(self):
        if (self.__size == 0):
            print("")
            return
        for k in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for l in range(0, self.__position[0]):
                    print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")

    def __repr__(self):
        self.my_print()
        return ""

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or value[0] < 0 or
                not isinstance(value[1], int) or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
