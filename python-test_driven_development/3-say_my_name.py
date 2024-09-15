#!/usr/bin/python3
"""
2-matrix_divided
This is a module for dividing all of the elements
in a matrix by the given divisor
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name prints the given names
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {}".format(first_name), end=" ")
    print(last_name)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
