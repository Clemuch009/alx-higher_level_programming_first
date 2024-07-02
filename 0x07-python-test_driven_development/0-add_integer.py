#!/usr/bin/python3
"""
adding

"""
def add_integer(a , b=98):
    """
    addation

    """
    if not isinstance(a ,(float, int)):
        """
        warning

        """
        raise TypeError ("a must be an integer")

    if not isinstance(b ,(float ,int)):
        """
        warning

        """
        raise TypeError ("b must be an integer")

    return int(a) + int (b)
