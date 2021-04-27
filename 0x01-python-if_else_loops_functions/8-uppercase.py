#!/usr/bin/python3
def uppercase(str):
    res = ""
    lower_ascii = 0
    for i in range(0, len(str)):
        lower_ascii = ord(str[i])
        if lower_ascii >= 97 and lower_ascii <= 122:
            res += chr(lower_ascii - 32) # Get Ascii of lowercase and substract 32 to get luppercase
            continue
        res += str[i]

    print(res)