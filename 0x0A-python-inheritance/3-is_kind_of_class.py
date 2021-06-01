#!/usr/bin/python3
''' Executable Command '''


def is_kind_of_class(obj, a_class):
    ''' is kind of class '''
    return isinstance(obj, a_class) or issubclass(a_class, type(obj))
