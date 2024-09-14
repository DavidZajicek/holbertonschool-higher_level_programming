#!/usr/bin/python3

def safe_print_division(a, b):
    value = 0
    try:
        value = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        return None
    finally:
        print("Inside Result: {:.1f}".format(value))
        return value


def main():
    has_been_print = safe_print_division(1, 0)
    print(has_been_print)


if __name__ == "__main__":
    main()
