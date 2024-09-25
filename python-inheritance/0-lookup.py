#!/usr/bin/python3
"""
0. Lookup
mandatory
Write a function that returns the list of available attributes and methods
of an object:
"""


def lookup(obj: object):
    """
    return list of attributes and methods
    """
    return list(dir(obj))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
