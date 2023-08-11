#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        if len(sys.argv) == 2:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(len(sys.argv) - 1))
        i = 0
        for ar in sys.argv:
            if i != 0:
                print("{:d}: {:s}".format(i, ar))
            i = i + 1
