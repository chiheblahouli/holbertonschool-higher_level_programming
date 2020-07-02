#!/usr/bin/python3
"""
prints text
"""



def append_write(filename="", text=""):
    """ write text """
    with open(filename, 'a', encoding='utf8') as Fichier:
       N = file.write(text)
    return(N)
