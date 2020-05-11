#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = dict()
    for key, elay in a_dictionary.items():
        new_list.update({key: (elay * 2)})
    return new_list
