#!/usr/bin/python3
''' Executable command '''


from models.base import Base


class Rectangle(Base):
    ''' Defines a Rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Class constructor '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        ''' Returns the area '''
        return self.width * self.height

    def display(self):
        ''' Displays the rectangle '''
        print('\n' * self.y, end="")
        for i in range(0, self.height):
            print(' ' * self.x, end="")
            print("#" * self.width)

    def update(self, *args):
        ''' Updates the variables values
        I did not want to do this way but...
        life has difficult choices '''
        for i in range(0, len(args)):
            if (i == 0):
                self.id = args[0]
            elif (i == 1):
                self.width = args[1]
            elif (i == 2):
                self.height = args[2]
            elif(i == 3):
                self.x = args[3]
            elif (i == 4):
                self.y = args[4]

    def __str__(self):
        ''' string representation of the instance '''
        id = self.id
        w = self.width
        h = self.height
        x = self.x
        y = self.y
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(id, x, y, w, h)

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @width.setter
    def width(self, value):
        ''' width setter '''
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        ''' height setter '''
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        ''' x setter '''
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        ''' y setter '''
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
