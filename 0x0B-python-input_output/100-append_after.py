#!/usr/bin/python3
''' function that inserts a line of text to a file, after each line'''


def append_after(filename="", search_string="", new_string=""):
    ''' work '''
    s = ''
    with open(filename, 'r') as f:
        for line in f:
            s += line
            if search_string in line:
                s += new_string

    with open(filename, 'w') as f:
        f.write(s)
