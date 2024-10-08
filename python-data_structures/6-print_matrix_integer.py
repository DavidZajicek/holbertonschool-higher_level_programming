#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            if y != x[0]:
                print("", end=" ")
            print("{:d}".format(y), end="")
        print("")


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)


if __name__ == "__main__":
    main()
