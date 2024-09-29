#!/usr/bin/python3
"""
1. Shapes, Interfaces, and Duck Typing
mandatory
Arf, Bark, Meow
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Shape
    """
    @abstractmethod
    def area(self):
        return NotImplemented

    @abstractmethod
    def perimeter(self):
        return NotImplemented


class Circle(Shape):
    """
    Circle
    """

    def __init__(self, radius: int) -> None:
        self.__radius = radius

    def area(self):
        return pi * (self.__radius * self.__radius)

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
    Rectangle
    """

    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)


def shape_info(shape: Shape):
    """
    Shape Info
    """
    print(f'Area: {shape.area()}\nPerimeter: {shape.perimeter()}')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
