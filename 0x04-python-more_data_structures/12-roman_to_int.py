#!/usr/bin/python3
#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return None
    int_val = 0
    current_val = 0
    prev_val = 0
    translation = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(0, len(roman_string)):
        current_val = translation[roman_string[i]]
        int_val += current_val
        if prev_val < current_val and prev_val != 0:
            int_val -= prev_val * 2
        prev_val = current_val

    return int_val
