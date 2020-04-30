#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    list = sys.argv
    cross = len(list) - 1
    if cross == 0:
        print("{:d} arguments.".format(cross))
    elif cross == 1:
        print("{:d} argument:".format(cross))
    else:
        print("{:d} arguments:".format(cross))
    if cross > 0:
        for i in range(len(list)):
            if i > 0:
                print("{:d}: {}".format(i, list[i]))
