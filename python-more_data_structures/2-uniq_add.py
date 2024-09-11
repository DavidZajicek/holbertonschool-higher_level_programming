#!/usr/bin/python3

def uniq_add(my_list: list = []):
    new_list = []
    result = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
            result += i
    return result


def main():
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))


if __name__ == "__main__":
    main()
