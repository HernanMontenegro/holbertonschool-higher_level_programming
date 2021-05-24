#!/usr/bin/python3
"""
Executable command
"""


class Rectangle:
    """ Class that defines a
    rectangle
    """

    number_of_instances = 0
    print_symbol = "#"
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """ Called when a new instance is created """

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        final_str = ""

        for i in range(0, self.__height):
            final_str += (str(self.print_symbol) * self.__width)
            if (i != self.__height - 1):
                final_str += '\n'

        return final_str

    def __repr__(self):
        width_str = str(self.__width)
        height_str = str(self.__height)
        final_str = "Rectangle(" + width_str + ", " + height_str + ")"
        return final_str

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        return

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (type(rect_1) != Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (type(rect_2) != Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        re1_area = rect_1.area()
        re2_area = rect_2.area()

        if ((re1_area > re2_area) or (re1_area == re2_area)):
            return rect_1
        else:
            return rect_2

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value
