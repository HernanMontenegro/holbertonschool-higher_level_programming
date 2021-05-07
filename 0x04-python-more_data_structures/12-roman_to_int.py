#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return None
    int_val = 0
    first_val = 0
    last_val = 0
    start_sum_index = 0
    translation = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    first_val = translation[roman_string[0]]
    last_val = translation[roman_string[len(roman_string) - 1]]

    if (first_val <  last_val):
        for i in range(0, len(roman_string)):
            int_val -= first_val
            if (first_val < translation[roman_string[i + 1]]):
                    start_sum_index = i + 1
                    break
    
    for i in range(start_sum_index, len(roman_string)):
        int_val += translation[roman_string[i]]

    return int_val
