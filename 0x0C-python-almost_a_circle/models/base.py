#!/usr/bin/python3
''' Executable command '''


class Base:
    ''' Base class definition '''

    __nb_objects = 0
    def __init__(self, id=None):
        ''' Class constructor '''
        if (id != None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
