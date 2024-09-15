#!/usr/bin/python3
"""
2-matrix_divided
This is a module for dividing all of the elements 
in a matrix by the given divisor
"""


def matrix_divided(matrix, div):
    """
    divide all of the elements in the given matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    row_length = 0
    result = []
    row_length = len(matrix[0])
    for row in matrix:
        row_result = []
        if len(row) != row_length:
            raise TypeError(
                'Each row of the matrix must have the same size')
        for i in row:
            if isinstance(i, (int, float)):
                row_result.append(round(i / div, 2))
                continue
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        result.append(row_result)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
