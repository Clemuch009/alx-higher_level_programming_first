#!/usr/bin/python3


def weight_average(my_list=[]):
    sum = 0
    divisor = 0
    for tup in my_list:
        if len(tup) != 2:
            return 0
        sum = sum + tup[0] * tup[1]
        divisor = divisor + tup[1]
    if divisor == 0:
        return 0
    return sum / divisor
