#!/usr/bin/python3
''' Executable command '''


import json


def class_to_json(obj):
    ''' returns the dictionary description with simple data structure
    for JSON
    '''
    return obj.__dict__
    