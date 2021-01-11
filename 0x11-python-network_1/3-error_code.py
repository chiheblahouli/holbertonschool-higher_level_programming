#!/usr/bin/python3
"""
A request to URL fir displays
"""
import urllib.error as error
import urllib.request as request
import sys

if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
