#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set()
    if my_list:
        for element in my_list:
            new_list.add(element)
    return sum(new_list)
