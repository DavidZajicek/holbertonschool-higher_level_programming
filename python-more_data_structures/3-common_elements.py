#!/usr/bin/python3

def common_elements(set_1, set_2):
    return { c for c in set_1 if c in set_2 }


def main():
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))


if __name__ == "__main__":
    main()
