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

    def to_json(self, attrs=None):
        """
        Return self as serialisable json dict
        """
        if attrs is not None:
            return {x: y for (x, y) in self.__dict__.items() if x in attrs}
        return self.__dict__

    def reload_from_json(self, json: dict):
        """
        Overwrite Student Data
        """
        for (key, value) in json:
            if key == "first_name":
                self.first_name = value
            if key == "last_name":
                self.last_name = value
            if key == "age":
                self.age = value


if __name__ == "__main__":
    pass
