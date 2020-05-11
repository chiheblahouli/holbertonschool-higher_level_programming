#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for index, i in enumerate(list):
            print("{:d}".format(i), end="")
            if (index < len(list) - 1):
                print("{}".format(" "), end="")
        print()
