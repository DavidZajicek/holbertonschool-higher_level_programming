#!/usr/bin/python3
"""
2. Exact same object
mandatory
Write a function that returns True if the object is exactly an instance of
the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    check is same class
    """
    return True if type(obj) == type(a_class) else False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
