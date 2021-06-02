#!/usr/bin/python3
"""descripcion de la funcion,
    lo que hace y para que sirve
    """

import sys
import json
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

myfile = 'add_item.json'

mylist = []

if os.path.exists(myfile) and os.path.getsize(myfile) > 0:
    mylist = load_from_json_file(myfile)

if len(sys.argv) > 1:
    for element in sys.argv[1:]:
        mylist.append(element)

save_to_json_file(mylist, myfile)
