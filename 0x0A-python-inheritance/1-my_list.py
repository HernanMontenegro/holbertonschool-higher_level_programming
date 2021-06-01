#!/usr/bin/python3
''' Executable command '''


class MyList(list):
    ''' Class that has my own list methods '''

    def print_sorted(self):
        ''' prints a list in ascending sort '''
        print(sorted(self))
