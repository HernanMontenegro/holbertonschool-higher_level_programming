#!/usr/bin/python3
''' Executable command '''


from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Defines a square '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        ''' string representation of object '''
        id = self.id
        size = self.width
        x = self.x
        y = self.y
        return "[Square] ({}) {:d}/{:d} - {:d}".format(id, x, y, size)
