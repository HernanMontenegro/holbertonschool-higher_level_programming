#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for element in sorted(a_dictionary):
        print("{}: {}".format(element, a_dictionary[element]))
