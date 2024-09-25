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

    def integer_validator(self, name, value):
        """
        Validates value
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if not value:
            raise ValueError(f'{name} must be greater than 0')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
