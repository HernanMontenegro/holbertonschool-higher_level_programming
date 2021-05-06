#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()

    for elem in a_dictionary:
        new_dictionary[elem] = a_dictionary[elem] * 2

    return new_dictionary
