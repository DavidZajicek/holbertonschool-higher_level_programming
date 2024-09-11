#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    result = {c for c in set_1 if c not in set_2}
    result.update({c for c in set_2 if c not in set_1})
    return result


def main():
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = only_diff_elements(set_1, set_2)
    print(sorted(list(c_set)))


if __name__ == "__main__":
    main()
