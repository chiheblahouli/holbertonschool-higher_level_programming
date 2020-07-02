#!/usr/bin/python3
"""
read and ope the file
"""


def write_file(filename="", text=""):
    """
    write the new file name 
    """
    with open(filename, 'w', encoding='utf-8') as Fichier:
        N = file.write(text)
    return(N)
