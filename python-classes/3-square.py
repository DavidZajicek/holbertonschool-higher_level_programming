#!/usr/bin/python3
"""
3. Area of a square
mandatory
Write a class Square that defines a square by: (based on 2-square.py)
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
        # print(f"{self.__dict__}\n{self.__size}")

    def area(self):
        """
        Returns the total size of the Square Instance
        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square = Square(3)
