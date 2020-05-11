#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for egal in my_string:
        if (egal != 'C' and egal != 'c'):
            new_string = new_string + egal
    return (new_string)
