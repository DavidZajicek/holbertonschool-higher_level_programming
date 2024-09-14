#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False


def main():
    value = ""
    has_been_print = safe_print_integer(value)
    print(has_been_print)


if __name__ == "__main__":
    main()
