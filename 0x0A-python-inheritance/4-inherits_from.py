#!/usr/bin/python3
"""
checks if the object is an instance of, or if the object is an instance
"""


def inherits_from(obj, a_class):
    """ returns true if object is a subclass of a class """
    return(issubclass(type(obj), a_class))
