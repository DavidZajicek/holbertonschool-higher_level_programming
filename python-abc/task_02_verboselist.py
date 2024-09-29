#!/usr/bin/python3
"""
2. Extending the Python List with Notifications
mandatory
Arf, Bark, Meow
"""

from typing import Iterable, SupportsIndex


class VerboseList(list):
    """
    List that prints extra info when used
    """

    def append(self, obj) -> None:
        print(f'Added [{obj}] to the list.')
        return super().append(obj)

    def extend(self, iterable: Iterable) -> None:
        print(f'Extended the list with [{len(iterable)}] items.')
        return super().extend(iterable)

    def remove(self, value) -> None:
        try:
            super().remove(value)
            print(f'Remove [{value}] from the list.')
        except ValueError:
            print(f'Value [{value}] not found in list')

    def pop(self, index: SupportsIndex = -1):
        try:
            value = self[index]
            print(f'Popped {value} from the list.')
            return super().pop(index)
        except IndexError:
            print(f'Index [{index}] not in list.')


if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)
    vl.remove('a')
    vl.pop(7)
