#!/usr/bin/python3
"""
12. Pascal's Triangle
mandatory
.
"""


def factorial(n):
    """
    factorial
    """
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def combination(n, r):
    """
    combination
    """
    return int((factorial(n)) / ((factorial(r)) * factorial(n - r)))


def pascal_triangle(n):
    """
    Pascal Triangle
    """
    if n <= 0:
        return []

    triangle = [[]]
    triangle[0].append(1)
    for _ in range(1, n):
        row = []
        temp = [0] + triangle[-1] + [0]
        for j in range(len(triangle) + 1):
            row.append(temp[j] + temp[j + 1])
        triangle.append(row)
    return (triangle)


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(6))
