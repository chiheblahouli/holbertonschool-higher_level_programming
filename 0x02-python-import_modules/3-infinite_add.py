#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    list = sys.argv
    cross = len(list) - 1
    result = 0
    if cross > 0:
            for i in range(len(list)):
                if i > 0 and list[i]:
                    result += int(list[i])
    print(result)
