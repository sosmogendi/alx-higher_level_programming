#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    final = 0
    prev_value = 0

    for c in reversed(roman_string):
        value = roman_values.get(c, 0)

        if value >= prev_value:
            final += value
        else:
            final -= value

        prev_value = value

    return final
