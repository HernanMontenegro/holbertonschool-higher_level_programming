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
        array = []
        if (json_string is None):
            return array
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Saves the json representation
        of 2 intances who inherits from me '''
        s = "[]"
        with open(file="{}.json".format(cls.__name__), mode="w") as f:
            if (list_objs is None):
                f.write(s)
                return
            s = "["
            for i in range(0, len(list_objs)):
                s += list_objs[i].to_json_string(list_objs[i].to_dictionary())
                if (i != len(list_objs) - 1):
                    s += ", "
            s += "]"
            f.write(s)

    @classmethod
    def create(cls, **dictionary):
        ''' Creates a new instance from a dictionary '''
        new_instance = cls(12, 13)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        j_list = []
        ins_list = []
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                j_list = cls.from_json_string(f.read())
            for item in j_list:
                ins_list.append(cls.create(**item))
        except:
            return ins_list
        return ins_list
