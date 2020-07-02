#!/usr/bin/python3
"""
number of lines
"""


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    with open(filename, 'r', encoding='utf8') as Fichier:
         Count = 0  
        for lines in Fichier:
            Count += 1
    return Count
