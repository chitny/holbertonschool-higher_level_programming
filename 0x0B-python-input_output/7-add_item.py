#!/usr/bin/python3
"""descripcion de la funcion,
    lo que hace y para que sirve
    """

import sys
import json
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

myfile = 'add_item.json'

mylist = []

if (path.exists(myfile)):
    mylist = load_from_json_file(myfile)

for element in range(1, len(argv)):
    mylist.append(argv[element])

save_to_json_file(mylist, myfile)
