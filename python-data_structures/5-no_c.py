#!/usr/bin/python3

def no_c(my_string: str):
    string_array = list(my_string)
    result = []
    for c in string_array:
        if ord(c) != 67 and ord(c) != 99:
            result.append(c)
    return "".join(result)


def main():
    my_string = "string hereCccC"
    print("{}".format(no_c(my_string)))
    print("{}".format(my_string))


if __name__ == "__main__":
    main()
