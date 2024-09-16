#!/usr/bin/python3
"""
1. Real definition of a rectangle
mandatory
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    A class that defines a Rectangle
    """
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width: int = 0, height: int = 0) -> None:
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self) -> str:
        result = []
        if self.width == 0 or self.height == 0:
            return ""
        for _ in range(self.height):
            for _ in range(self.width):
                result.append(str(self.print_symbol))
            result.append('\n')
        return "".join(result[:-1])

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @width.setter
    def width(self, width: int = 0):
        """
        Setter for width
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @height.setter
    def height(self, height: int = 0):
        """
        Setter for height
        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """
        Return the total area of the rect
        """
        return self.height * self.width

    def perimeter(self):
        """
        Return the total perimeter of the rect
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height + self.width) * 2

    def bigger_or_equal(self, rect_2):
        """
        Return the bigger rect
        Return self if both have the same area value
        """
        if not isinstance(self, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        return self if self.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Return a new Square
        """
        return Rectangle(size, size)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
