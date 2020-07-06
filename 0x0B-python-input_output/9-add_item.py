#!/usr/bin/python3
""" A script that reads and inserts """


if __name__ == "__main__":
    import sys
    import os
    save_json = __import__('7-save_to_json_file').save_to_json_file
    load_json = __import__('8-load_from_json_file').load_from_json_file

    inputs = sys.argv
    my_list = list()
    if os.path.isfile("add_item.json"):
        my_list = load_json("add_item.json")
    for i in range(1, len(inputs)):
        my_list.append(inputs[i])
    save_json(my_list, "add_item.json")
