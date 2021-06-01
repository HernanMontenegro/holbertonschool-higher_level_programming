#!/usr/bin/python3
''' Executable command '''


class BaseGeometry:
    ''' A Base Geometry class '''
    def area(self):
        ''' the area of the shape '''
        raise Exception("area() is not implemented")
