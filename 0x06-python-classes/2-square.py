#!/usr/bin/python3
"""
2-square
contains class Square that defines a square
"""


class Square:
    """ creates an __init__ method with size instance """
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
