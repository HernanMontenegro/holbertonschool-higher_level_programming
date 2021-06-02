#!/usr/bin/python3
''' Executable command '''


def read_file(filename=""):
    ''' Reads a text file (UTF8) and
    prints it to STDOUT
    '''
    with open(filename, 'r') as file:
        print(file.read(), end="")
