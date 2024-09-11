#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result


def main():
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, ())
    print(new_tuple)


if __name__ == "__main__":
    main()
