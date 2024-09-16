#!/usr/bin/python3
"""
1. Real definition of a rectangle
mandatory
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    A class that defines a Rectangle
    """

    def __init__(self, width: int = 0, height: int = 0) -> None:
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @width.setter
    def width(self, width: int = 0):
        """
        Setter for width
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @height.setter
    def height(self, height: int = 0):
        """
        Setter for height
        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height


if __name__ == "__main__":
    import doctest
    doctest.testmod()
