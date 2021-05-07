#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return None
    prev = 0
    int_val = 0

    translation = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    for i in range(len(roman_string)-1, -1, -1):
        if translation[roman_string[i]] >= prev:
            int_val += translation[roman_string[i]]
        else:
            int_val -= translation[roman_string[i]]

        prev = translation[roman_string[i]]

    return int_val
