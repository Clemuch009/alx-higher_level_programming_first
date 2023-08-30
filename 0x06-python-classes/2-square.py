#!/usr/bin/python3


class Square:
    ''' class representing a square
    '''
    def __init__(self, size=0):
        ''' method initializing a square of size size
        '''
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
