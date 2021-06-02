#!/usr/bin/python3
''' Executable command '''


class Student:
    ''' Student class definition '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' retrieves a dictionary representation '''
        my_dict = {}
        if (attrs != None and type(attrs) == list):
            for item in attrs:
                if (type(item) != str):
                    my_dict = self.__dict__
                    break
                if (item in self.__dict__):
                    my_dict[item] = self.__dict__[item]
        else:
            my_dict = self.__dict__
        return my_dict

    def reload_from_json(self, json):
        for key in json:
            self.__dict__[key] = json[key]
