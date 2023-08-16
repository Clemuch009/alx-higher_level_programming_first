#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is not True:
        return 0
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for let in roman_string:
        if let not in dictionary:
            return 0
        if dictionary[let] > total:
            total = dictionary[let] - total
        elif dictionary[let] > prev:
            total = total + dictionary[let] - prev * 2
        else:
            total = dictionary[let] + total
        prev = dictionary[let]
    return total
