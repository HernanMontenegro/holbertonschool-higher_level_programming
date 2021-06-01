#!/usr/bin/python3
''' Executable command '''


class BaseGeometry:
    ''' A Base Geometry class '''
    def area(self):
        ''' the area of the shape '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates an int value '''
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


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
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
