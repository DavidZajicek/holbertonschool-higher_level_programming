#!/usr/bin/python3
"""
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename: str = ""):
    """
    Read File
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())


if __name__ == "__main__":
    read_file("/home/holberton/test.txt")
