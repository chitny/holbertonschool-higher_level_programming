#!/usr/bin/python3
"""description"""


import json
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
newlist = []
myfile = "add_item.json"
try:
    newlist = load_from_json_file(myfile)
except FileNotFoundError:
    save_to_json_file(newlist, myfile)

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        newlist.append(sys.argv[i])
save_to_json_file(newlist, myfile)
