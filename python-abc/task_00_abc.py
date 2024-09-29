#!/usr/bin/python3
"""
0. Abstract Animal Class and its Subclasses
mandatory
Arf, Bark, Meow
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal - The Living Tombstone
    """
    @abstractmethod
    def sound(self):
        """
        Not Implemented abstract method
        """
        return NotImplemented


class Dog(Animal):
    """
    Dog
    """

    def sound(self):
        """
        Bark
        """
        return "Bark"


class Cat(Animal):
    """
    Cat
    """

    def sound(self):
        """
        Meow
        """
        return "Meow"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
