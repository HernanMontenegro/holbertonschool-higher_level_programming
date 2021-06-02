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
                    continue
                if (item == "first_name"):
                    my_dict['first_name'] = self.first_name
                elif (item == "last_name"):
                    my_dict['last_name'] = self.last_name
                elif (item == "age"):
                    my_dict['age'] = self.age
        else:
            my_dict = self.__dict__
        return my_dict
