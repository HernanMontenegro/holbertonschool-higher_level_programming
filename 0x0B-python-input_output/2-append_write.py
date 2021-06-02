#!/usr/bin/python3
''' Executable command '''


def append_write(filename="", text=""):
    ''' Appends a string to a text file (UTF8)
    and returns the number of characters added
    '''
    with open(filename, 'a+') as file:
        file.write(text)

    return (len(text))
