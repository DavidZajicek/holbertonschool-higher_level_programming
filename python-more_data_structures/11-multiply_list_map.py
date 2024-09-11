#!/usr/bin/python3


def multiply_list_map(my_list: list = [], number=0):
    return [x*number for x in my_list].copy()


def main():
    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)


if __name__ == "__main__":
    main()
