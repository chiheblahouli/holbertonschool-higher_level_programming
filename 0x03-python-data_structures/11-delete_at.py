#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0 or len(my_list) <= idx or idx < 0:
        return my_list
    elif my_list is not None:
        my_list.remove(idx + 1)
    return my_list
