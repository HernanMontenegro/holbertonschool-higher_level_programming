#!/usr/bin/python3
''' Executable command '''


import json


class Base:
    ''' Base class definition '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Class constructor '''
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns json string representation of a
        dictionaries list '''
        if (list_dictionaries is None):
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of JSON string
        representation '''
        

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Saves the json representation
        of 2 intances who inherits from me '''
        json_str = "[]"
        with open(file="{}.json".format(cls.__name__), mode="w") as f:
            if (list_objs is None):
                f.write(json_str)
                return
            json_str = "["
            for i in range(0, len(list_objs)):
                json_str += list_objs[i].to_json_string(list_objs[i].to_dictionary())
                if (i != len(list_objs) - 1):
                    json_str += ", "
            json_str += "]"
            f.write(json_str)
