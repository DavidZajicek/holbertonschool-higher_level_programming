#!/usr/bin/python3
def multiply_list_map(my_list: list = [], number=0):
    return list(map(lambda x: x*number, my_list)).copy()
