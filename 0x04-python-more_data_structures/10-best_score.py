#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    is_first = True
    big = None
    for key in a_dictionary:
        if is_first is True:
            is_first = False
            big = key
        else:
            if a_dictionary[key] > a_dictionary[big]:
                big = key
    return big
