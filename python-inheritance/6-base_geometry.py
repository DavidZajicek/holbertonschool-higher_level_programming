#!/usr/bin/python3
"""
5. Geometry module
mandatory
Write an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    Base Geometry class (if you're naming it base, you're doing it wrong)
    """

    def area(self):
        """
        Unimplemented method
        """
        raise Exception('area() is not implemented')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
