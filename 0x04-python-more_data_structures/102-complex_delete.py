#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = a_dictionary.copy()
    for key, target_value in new_dic.items():
        if target_value == value:
            del a_dictionary[key]
    new_dic.copy()
    return new_dic
