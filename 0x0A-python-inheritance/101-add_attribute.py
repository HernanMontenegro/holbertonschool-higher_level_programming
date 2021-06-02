#!/usr/bin/python3
''' Executable Command '''


def add_attribute(obj, name, value):
    ''' Add attribute only if it can '''
    if (hasattr(obj, "__dict__") is False):
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
