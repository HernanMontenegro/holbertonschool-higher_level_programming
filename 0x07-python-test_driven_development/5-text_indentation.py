#!/usr/bin/python3
"""Executable command

    You can test this function in
    /test/5-text_indentation.txt
"""


def text_indentation(text):
    i = 0
    c = 'a'
    if (type(text) != str):
        raise TypeError("text must be a string")

    while i < len(text):
        c = text[i]
        print(c, end="")
        if (c == '.' or c == '?' or c == ':'):
            if (i == len(text) - 1):
                break
            print("\n")
            while (i < len(text)):
                if (text[i + 1] != ' '):
                    break
                i += 1
        i += 1
