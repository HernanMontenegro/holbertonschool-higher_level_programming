#!/usr/bin/python3
''' Executable command '''


def inherits_from(obj, a_class):
    ''' Inherits from '''
    if (type(obj) is a_class):
        return (False)
    return issubclass(type(obj), a_class)
