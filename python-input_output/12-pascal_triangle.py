#!/usr/bin/python3
"""
12. Pascal's Triangle
mandatory
.
"""
import math


def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))


def pascal_triangle(n):
    """
    Pascal Triangle
    """
    result = []

    for count in range(n):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        result.append(row)
    return result


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(6))
