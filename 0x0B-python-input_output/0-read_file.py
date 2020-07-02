#!/usr/bin/python3
"""
 function that reads a text file
"""


def read_file(filename=""):
"""
    Read file and prints
"""

    with open(filename, 'r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
