#!/usr/bin/python3
"""
adds all arguments to a Python
"""
import sys



save_to_json = __import__("7-save_to_json_file").save_to_json_file
load_from_json = __import__("8-load_from_json_file").load_from_json_file
except:
    load_from_json_file("add_item.json") = []
save_to_json_file(lst = load_from_json_file("add_item.json") + sys.argv[1:], "add_item.json")

