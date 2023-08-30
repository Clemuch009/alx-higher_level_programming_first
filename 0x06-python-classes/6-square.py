#!/usr/bin/python3
"""
6-square
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
    def __init__(self, size=0, position=(0, 0)):
        """ initializes instance attribute size and position """
        self.size = size
        self.position = position

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
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ retrieves position """
        return self.__position

    @position.setter
    def position(self, value):
        """
        - sets position
        - raise errors when value is not tuple of 2 positive integers
        """
        if isinstance(value, tuple) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[1], int) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print("")
        else:
            for p in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print("", end=" ")
                for k in range(self.__size):
                        print("#", end="")
                print("")
