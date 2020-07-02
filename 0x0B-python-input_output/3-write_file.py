#!/usr/bin/python3
"""
read and ope the file
"""


def write_file(filename="", text=""):
    """
    write the new file name 
    """
    with open(filename, 'w', encoding='utf8') as Fichier:
        N = Fichier.write(text)
    return(N)
