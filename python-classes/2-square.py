#!/usr/bin/python3
"""
2. Size validation
mandatory
Write a class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the
    message size must be an integer
if size is less than 0, raise a ValueError exception with the message
    size must be >= 0
You are not allowed to import any module
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


if __name__ == "__main__":
    my_square = Square(3)
