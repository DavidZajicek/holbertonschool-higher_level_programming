#!/usr/bin/python3

def max_integer(my_list: list = []):
    if len(my_list) == 0:
        return None
    pointer = my_list[0]
    for i in my_list:
        if i > pointer:
            pointer = i
    return pointer


def main():
    my_list = [-1, -2]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))


if __name__ == "__main__":
    main()
