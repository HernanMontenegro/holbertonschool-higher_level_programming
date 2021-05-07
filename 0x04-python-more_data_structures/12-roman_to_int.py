#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    value = 0
    if type(roman_string) is not str or roman_string is None:
        return (0)

    traduction = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for i in range(len(roman_string)):
        value = traduction[roman_string[i]]

        if i < (len(roman_string) - 1):
            if value < traduction[roman_string[i + 1]]:
                res -= value
            else:
                res += value
        else:
            res += value

    return (res)
