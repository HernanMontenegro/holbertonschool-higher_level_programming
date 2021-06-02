#!/usr/bin/python3
''' Executable Command '''


class MyInt(int):
    ''' Class MyInt '''

    def __eq__(self, value):
        ''' equal '''
        return(super().__ne__(value))

    def __ne__(self, value):
        ''' not equal '''
        return(super().__eq__(value))
