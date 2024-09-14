#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        except IndexError:
            if i != 0:
                print("")
            return IndexError
        except (TypeError, ValueError):
            i += 1
            continue
    print("")
    return i


def main():
    my_list = ["1", 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 1)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list_integers([], 0)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list_integers(my_list, 6 + 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list_integers(123, + 2)
    print("nb_print: {:d}".format(nb_print))


if __name__ == "__main__":
    main()
