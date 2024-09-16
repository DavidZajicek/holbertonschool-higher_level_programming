#!/usr/bin/python3
"""
1. Square with size
mandatory
Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
"""


class Square:
    """
    An empty class Square that defines a Square
    """

    def __init__(self, size: int = 3) -> None:
        """
        __init__ initialises an instance of the given class
        """
        self.__size = size
        # print(f"{self.__dict__}\n{self.__size}")


if __name__ == "__main__":
    my_square = Square(3)
