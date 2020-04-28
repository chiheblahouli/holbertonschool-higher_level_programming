#!/usr/bin/python3
for a in range(0, 9):
for c in range(a + 1, 10):
       if a != 8:
            print("{:d}{:d}".format(a, c), end=', ')
       else:
            print("{:d}{:d}".format(a, c)
