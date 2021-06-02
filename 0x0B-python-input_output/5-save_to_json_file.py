#!/usr/bin/python3
''' Executable command '''


import json


def save_to_json_file(my_obj, filename):
    ''' writes an Object to a text file, using a JSON representation '''
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
