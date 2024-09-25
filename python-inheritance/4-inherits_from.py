#!/usr/bin/python3
"""
2. Exact same object
mandatory
Write a function that returns True if the object is exactly an instance of
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    check is same class
    """
    return issubclass(obj, a_class)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
