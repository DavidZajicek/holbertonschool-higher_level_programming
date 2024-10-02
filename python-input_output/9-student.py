#!/usr/bin/python3
"""
9. Student to JSON
mandatory
Write a class Student that defines a student by:
"""


class Student():
    """
    Student
    """

    def __init__(self, first_name, last_name, age) -> None:
        """
        init tho
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return self as serialisable json dict
        """
        return self.__dict__


if __name__ == "__main__":
    pass
