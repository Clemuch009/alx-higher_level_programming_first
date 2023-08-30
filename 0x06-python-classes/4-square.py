#!/usr/bin/python3
"""
4-square
- contains class Square that defines a square
- returns the current square area
"""


class Square:
    """
    - creates __init__ method and area method
    - creates getter and setter for size
    """
    def __init__(self, size=0):
        """ initializes instance attribute size """
        self.size = size

    @property
    def size(self):
        """ retrieves size """
        return self.__size

    @size.setter
    def size(self, value):
        """
        - sets size
        - raise errors when size is not int or size is less than 0
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size
