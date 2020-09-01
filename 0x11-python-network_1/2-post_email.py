#!/usr/bin/python3
"""
get value of x-Request-Id
"""
from sys import argv
import urllib.request
if __name__ == "__main__":

    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))

