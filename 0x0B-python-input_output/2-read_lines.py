#!/usr/bin/python3
""" print number of lines """


def read_lines(filename="", nb_lines=0):
    """ print filename to open and read """
    with open(filename, encoding="utf-8") as Fichier:
        if nb_lines <= 0:
            print("{}".format(Fichier.read()), end="")
        else:
            for lines in range(nb_lines):
                print(file.readline(), end="")
