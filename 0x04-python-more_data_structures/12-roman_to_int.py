#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return None
    int_val = 0
    current_val = 0
    next_val = 0
    i = 0

    translation = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    while i < len(roman_string):
        current_val = translation[roman_string[i]]
        if i + 1 < len(roman_string):
            next_val = translation[roman_string[i + 1]]

        if next_val != 0 and roman_string[i:i+2] in translation:
            int_val += translation[roman_string[i:i+2]]
            i += 2
        else:
            int_val += current_val

        current_val = 0
        next_val = 0
        i += 1

    return int_val
