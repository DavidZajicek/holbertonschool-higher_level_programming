#!/usr/bin/python3

def square_matrix_simple(matrix: list = []):
    new_matrix: list = []
    for x in range(0, len(matrix)):
        new_matrix.append([])
        for y in range(0, len(matrix[x])):
            new_matrix[x].append(matrix[x][y] * matrix[x][y])
    return new_matrix


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)


if __name__ == "__main__":
    main()
