#!/usr/bin/python3
"""
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool) -> None:
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        # Your code here to serialize and save data to the specified file
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        # Your code here to load and deserialize data from the specified file
        with open(filename, "rb") as file:
            try:
                return pickle.load(file)
            except (pickle.UnpicklingError, EOFError):
                return None

    def display(self):
        print(
            f'Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}')


if __name__ == "__main__":
    # Create an instance of CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("data.json")
    print("\nDeserialized Object:")
    new_obj.display()
