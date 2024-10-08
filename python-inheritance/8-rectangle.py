#!/usr/bin/python3
"""
8. Rectangle
mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle
    """

    def __init__(self, width, height):
        """
        init
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height


if __name__ == "__main__":
    import doctest
    doctest.testmod()
