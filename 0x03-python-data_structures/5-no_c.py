#!/usr/bin/python3


def no_c(my_string):
    num_c = my_string.count('c')
    num_C = my_string.count('C')
    for i in range(0, num_c):
        index = my_string.index('c')
        my_string = my_string[:index] + my_string[index + 1:]
    for i in range(0, num_C):
        index = my_string.index('C')
        my_string = my_string[:index] + my_string[index + 1:]
    return my_string
