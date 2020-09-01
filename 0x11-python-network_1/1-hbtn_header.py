#!/usr/bin/python3
"""
displays the value of the X-Request-Id
"""
if __name__ == "__main__":
import urllib.request
from sys import argv
    req = request.Request(argv[1])
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
