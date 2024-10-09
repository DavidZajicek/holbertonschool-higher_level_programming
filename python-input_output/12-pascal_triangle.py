#!/usr/bin/python3
"""
12. Pascal's Triangle
mandatory
.
"""


def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def combination(n, r):
    return int((factorial(n)) / ((factorial(r)) * factorial(n - r)))


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
