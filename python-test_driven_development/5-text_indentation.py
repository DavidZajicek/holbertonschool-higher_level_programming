#!/usr/bin/python3
"""
2-matrix_divided
This is a module for dividing all of the elements
in a matrix by the given divisor
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each . ? :
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    string = list(text)
    flag = False

    for c in string:
        if c == '.' or c == '?' or c == ':':
            flag = True
            print("{}".format(c), end="\n\n")
            continue
        elif c == " " and flag or c == "\\" and flag:
            continue
        else:
            flag = False
        if not flag:
            print("{}".format(c), end="")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
