#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    t_or_f = []
    for i in my_list:
        if i % 2 == 0:
            t_or_f.append(True)
        else:
            t_or_f.append(False)
    return t_or_f
