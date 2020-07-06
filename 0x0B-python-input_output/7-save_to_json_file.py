#!/usr/bin/python3
import json
"""
The text file using JSON representation
"""


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file """
    with open(filename, "w", encoding="utf8") as Fichier:
        json.dump(my_obj, Fichier)
