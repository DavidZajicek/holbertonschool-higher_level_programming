#!/usr/bin/python3
"""
12. Pascal's Triangle
mandatory
.
"""


def pascal_triangle(n):
    """
    Pascal Triangle
    """
    if n <= 0:
        return []
    


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
