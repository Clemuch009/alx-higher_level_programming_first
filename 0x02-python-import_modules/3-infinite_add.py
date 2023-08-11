#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    sum = 0
    bool = 0
    for ar in argv:
        if bool == 1:
            sum = sum + int(ar)
        bool = 1

    print(sum)
