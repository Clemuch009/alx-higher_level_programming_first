#!/usr/bin/python3


class Square:
    ''' class representing a square
    '''
    def __init__(self, size=0):
        ''' method initializing a square of size size
        '''
        self.size = size

    @property
    def size(self):
        ''' method that returns the size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' method that sets the size of the square
        '''
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        ''' method that returns area of the square
        '''
        return self.__size * self.__size

    def my_print(self):
        ''' method that prints the square
        '''
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.size):
                print('#', end='')
            print()
