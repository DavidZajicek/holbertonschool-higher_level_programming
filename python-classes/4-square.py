#!/usr/bin/python3
"""
4. Access and update private attribute
mandatory
Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """
    A class called Square that defines a Square
    """

    def __init__(self, size: int = 0) -> None:
        """
        __init__ initialises an instance of the given class
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Returns the total area of the Square Instance
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Returns the size of the Square Instance
        """
        return self.__size

    @size.setter
    def size(self, value: int = 0):
        """
        Returns the size of the Square Instance
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value


if __name__ == "__main__":
    my_square = Square(3)
