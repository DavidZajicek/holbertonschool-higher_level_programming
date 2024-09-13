#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
        except IndexError:
            if i != 0:
                print("")
            return i
        except TypeError:
            return i
    if i > 0:
        print("")
    return i


def main():
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 1)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list([], 0)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list,  + 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(123, + 2)
    print("nb_print: {:d}".format(nb_print))


if __name__ == "__main__":
    main()
