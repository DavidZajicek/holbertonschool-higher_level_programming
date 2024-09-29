#!/usr/bin/python3
"""
3. CountedIterator - Keeping Track of Iteration
mandatory
Arf, Bark, Meow
"""
from abc import ABC, abstractmethod


class CountedIterator(ABC):
    """
    Counted Iterator
    """

    def __init__(self, some_iterable) -> None:
        self.__counter = 0
        self.iterator = iter(some_iterable)

    def get_count(self):
        return self.__counter

    def __iter__(self):
        return self

    def __next__(self):
        current = next(self.iterator)
        if current is not None:
            self.__counter += 1
        return current


if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(
                f"Got {item}, total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")
