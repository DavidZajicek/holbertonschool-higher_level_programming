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


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json([])
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
