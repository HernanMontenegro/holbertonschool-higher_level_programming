#!/usr/bin/python3
''' Executable command '''


from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Defines a square '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Class constructor '''
        super().__init__(size, size, x, y, id)
        self.size = size
    
    def __str__(self):
        ''' string representation of object '''
        id = self.id
        size = self.size
        x = self.x
        y = self.y
        return "[Square] ({}) {:d}/{:d} - {:d}".format(id, x, y, size)

    def update(self, *args, **kwargs):
        ''' Updates the variables values
        I did not want to do this way but...
        life has difficult choices '''
        if (len(args) == 0 or args is None):
            for key in kwargs:
                if key == "id":
                    self.id = kwargs['id']
                elif key == "size":
                    self.size = kwargs['size']
                elif key == "x":
                    self.x = kwargs['x']
                elif key == "y":
                    self.y = kwargs['y']
            return
        for i in range(0, len(args)):
            if (i == 0):
                self.id = args[0]
            elif (i == 1):
                self.size = args[1]
            elif(i == 2):
                self.x = args[2]
            elif (i == 3):
                self.y = args[3]

    def to_dictionary(self):
        ''' Dictionary representation '''
        dicti = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return dicti

    @property
    def size(self):
        ''' size getter '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' size setter '''
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__size = value
