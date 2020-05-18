#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    val = 0.0
    try:
        val = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return val
    else:
        return None
