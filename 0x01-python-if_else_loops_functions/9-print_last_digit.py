#!/usr/bin/python3
def print_last_digit(number):
    m = abs(number) % 10
    print("{:d}".format(m), end="")
    return m
