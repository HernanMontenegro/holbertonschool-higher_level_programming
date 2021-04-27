#!/usr/bin/python3
def uppercase(str):
    lower_ascii = 0
    for i in range(0, len(str)):
        lower_ascii = ord(str[i])
        if lower_ascii >= 97 and lower_ascii <= 122:
            lower_ascii -= 32
        print('{}'.format(chr(lower_ascii)), end='')
    print("")
