#!/usr/bin/python3
"""
1. My list
mandatory
Write a class MyList that inherits from list:
"""


class MyList(list):
    """
    MyList inherits from list
    """

    def print_sorted(self):
        """
        print list sorted
        """
        return MyList(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
