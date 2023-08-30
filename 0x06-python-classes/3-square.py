#!/usr/bin/python3
"""
3-square
contains class Square that defines a square,
and returns the current square area
"""


class Square:
    """ creates __init__ method and area method """
    def __init__(self, size=0):
        """
        - initializes private instance attribute size
        - raises errors when size is not int or size is less than 0
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size
