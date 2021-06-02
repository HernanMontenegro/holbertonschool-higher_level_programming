#!/usr/bin/python3
''' Executable command '''


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import json
from sys import argv
from os import path

file_name = "add_item.json"
json_list = []

if (path.exists(file_name)):
    json_list = load_from_json_file(file_name)

for i in range(1, len(argv)):
    json_list.append(argv[i])
save_to_json_file(json_list, file_name)
