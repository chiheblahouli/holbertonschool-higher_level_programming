#!/usr/bin/python3
"""
class MyList that inherits from list
"""

class MyList(list):
    '''
        prints the list but in sorted ascending order
    '''
    def print_sorted(self):
        print(sorted(self))

