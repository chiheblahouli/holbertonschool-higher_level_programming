#!/usr/bin/python3
""" returns the number of lines in the files """


def number_of_lines(filename=""):
    """ counts the number of lines """
    Count = 0
    with open(filename, encoding="utf-8") as File:
        for lines in File:
            Count += 1
    return Count
