#!/usr/bin/python3
"""
0-add_integer
This is a module for adding integers together using python3.8
add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    Add two integers together
    """
    try:
        _a = int(a)
    except TypeError as err:
        raise TypeError("a must be an integer") from err
    try:
        if isinstance(b, str):
            raise TypeError
        _b = int(b)
    except (TypeError, ValueError) as err:
        raise NameError("b must be an integer") from err
    return _a + _b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
