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
        return self._width

    
    @width.setter
    def width(self, value):
        """verifying if is integer"""
        if  not isinstance (value , int):
            """error  warning"""
            raise TypeError("width must be an integer")
        """"value"""
        if  (width < 0):
            raise ValueError ("width must be >= 0")
        self._width = value

    

    @property
    def height(self):
        return self._height

    
    @height.setter
    def height(self, value):
        if not isinstance(value , int):
            raise TypeError ("height must be an integer")
        if (height < 0):
            raise ValueError ("height must be >= 0")
        self._heigth = value

    def area(self):
        area = width * width
        return area

    def perimeter (self):
        perimeter = (width + heigth) * 2
        if width == 0 or height == 0:
            perimeter = 0
        return perimeter
