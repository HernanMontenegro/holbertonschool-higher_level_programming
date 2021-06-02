#!/usr/bin/python3
''' Executable command '''

import json


def load_from_json_file(filename):
    ''' creates an Object from a JSON file '''
    with open(filename, 'r') as file:
        return json.loads(file.read())
