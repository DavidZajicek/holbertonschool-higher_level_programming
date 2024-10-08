#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list


def main():
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    element = 10
    print("{}".format(replace_in_list(my_list, idx, element)))


if __name__ == "__main__":
    main()
