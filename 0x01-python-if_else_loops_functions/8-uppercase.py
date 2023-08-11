#!/usr/bin/python3


def uppercase(str):
    for c in str:
        d = ord(c)
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            d = d - 32
        print('{:c}'.format(d), end='')
    print('')
