#!/usr/bin/python3

def delete_at(my_list: list = [], idx:int = 0):
    if idx < 0 or idx >= len(my_list):
        return None
    new_list: list = my_list.copy()
    my_list.clear()
    i = 0
    while i < len(new_list):
        if i != idx:
            my_list.append(new_list[i])
        i += 1
    return my_list


def main():
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)


if __name__ == "__main__":
    main()
