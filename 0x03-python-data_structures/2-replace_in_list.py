#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    new_list = my_list
    x = len(my_list)
    if idx >= 0 or idx < x:
        new_list[idx] = new_element
    return my_list
