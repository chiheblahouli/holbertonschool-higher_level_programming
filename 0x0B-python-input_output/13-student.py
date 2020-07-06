#!/usr/bin/python3
""" Student class with json method """


class Student:
    """ Student initialized by json """
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        att = dict()
        if not isinstance(attrs, list):
            return self.__dict__
        for keys in attrs:
            if not isinstance(keys, str):
                return self.__dict__
            if keys in self.__dict__:
                att.update({keys: self.__dict__[keys]})
        return att

    def reload_from_json(self, json):
        self.__dict__ = json
