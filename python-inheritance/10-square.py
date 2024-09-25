#!/usr/bin/python3
"""
9. Rectangle
mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Rectangle
    """

    def __init__(self, size):
        """
        init
        """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        Rectangle(size, size)

    def area(self):
        """
        area
        """
        return self.__size * self.__size

    def __str__(self):
        return f'[Rectangle] {self.__size}/{self.__size}'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
