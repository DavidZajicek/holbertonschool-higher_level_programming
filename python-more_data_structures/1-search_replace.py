#!/usr/bin/python3

def search_replace(my_list: list, search, replace):
    new_list: list = my_list.copy()
    for i in range(0, len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list


def main():
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)


if __name__ == "__main__":
    main()
