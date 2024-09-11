#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
        except (IndexError, TypeError):
            print("")
            return i
    print("")
    return i


def main():
    my_list = 3

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))


if __name__ == "__main__":
    main()
