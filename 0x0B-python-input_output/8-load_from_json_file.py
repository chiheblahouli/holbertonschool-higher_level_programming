#!/usr/bin/python3
"""
create an object from JSON file
"""
import json


def load_from_json_file(filename):
    """
    write a file
    """

    with open(filename, 'r', encoding='utf8') as Fichier:
        return json.load(Fichier)
