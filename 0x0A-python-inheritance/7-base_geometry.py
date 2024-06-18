#!/usr/bin/python3
"""basegeometry"""

class BaseGeometry:
    """instance of a class"""
    def __init__(self):
        """initialize"""
        pass


    def area(self):
        """raise exception"""
        raise Exception("area() is) not implemented")

    def interger_validator(self,name,value):
        """validates value"""
        self.name = str(name)
        self.value = value

        if  not isinstance(value,int):
            raise TypeError(f"{name} must be an integer")

        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
