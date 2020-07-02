#!/usr/bin/python3
"""
prints text
"""



def append_write(filename="", text=""):
    """ write text """
    with open(filename, 'a', encoding='utf-8') as Fichier:
       N = Fichier.write(text)
    return(N)
