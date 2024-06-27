#!/usr/bin/python3
"""rectangle class"""

class Rectangle:
    """initialization"""
    def __init__(self, width=0, height=0 ):
        """signing"""
        self._width = width
        self._height = height
        self.area = 0
        self.perimeter = 0


    @property
    def width(self):
        """get heigth"""
        return self._width


    @width.setter
    def width(self, value):
        """verifying if is integer"""
        if  not isinstance (value , int):
            """error  warning"""
            raise TypeError("width must be an integer")
        """"value"""
        if  (width < 0):
            """raise error"""
            raise ValueError ("width must be >= 0")
        self._width = value



    @property
    def height(self):
        """get heigth"""
        return self._height

