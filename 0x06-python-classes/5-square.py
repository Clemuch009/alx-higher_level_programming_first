#!/usr/bin/python3
"""
5-square
- contains class Square that defines a square
- returns the current square area
- prints in stdout the square with the character #
"""


class Square:
    """
    - creates __init__ method and area method
    - creates getter and setter for size
    - prints in stdout the square with the character #
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
        - raise errors when value is not int or value is less than 0
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character # """
        size = self.__size
        if size == 0:
            print("")
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
