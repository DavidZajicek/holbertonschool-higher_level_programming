#!/usr/bin/python3
"""
2. Append Write file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def append_write(filename: str = "", text: str = ""):
    """
    Append Write File
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    append_write("/home/holberton/test-write.txt", "test line\n")
