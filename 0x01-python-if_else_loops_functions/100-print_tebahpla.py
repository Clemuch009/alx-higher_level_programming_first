#!/usr/bin/python3

for c in range(ord('z'), ord('a'), -2):
    print('{:c}{:c}'.format(c, c - 33), end='')
