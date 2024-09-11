#!/usr/bin/python3

def divisible_by_2(my_list: list = []):
    new_list: list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list


def main():
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)
    print("Done {}", list_result)


if __name__ == "__main__":
    main()
