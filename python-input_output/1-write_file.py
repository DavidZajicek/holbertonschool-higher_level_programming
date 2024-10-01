#!/usr/bin/python3
"""
1. Write file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def write_file(filename: str = "", text: str = ""):
    """
    Write File
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)

if __name__ == "__main__":
    write_file("/home/holberton/test-write.txt", "test line\n")
