#!/usr/bin/python3

for let in range(ord('a'), ord('z')+1):
    if let != ord('e') and let != ord('q'):
        print("{:c}".format(let), end='')
