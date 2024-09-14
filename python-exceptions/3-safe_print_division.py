#!/usr/bin/python3

def safe_print_division(a, b):
    value = 0
    result = "Inside result: None"
    try:
        value = a / b
        result = "Inside result: {:.1f}".format(value)
    except ZeroDivisionError:
        return None
    finally:
        print(result)
    return value


def main():
    has_been_print = safe_print_division(1, 1)
    print(has_been_print)


if __name__ == "__main__":
    main()
