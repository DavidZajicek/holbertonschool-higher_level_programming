#!/usr/bin/python3
"""
2-matrix_divided
This is a module for dividing all of the elements
in a matrix by the given divisor
"""


def print_square(size):
    """
    this function prints a square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
