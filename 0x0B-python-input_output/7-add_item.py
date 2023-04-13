#!/usr/bin/python3
"""importing mods"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
"""adds all arguments to a Python list and save them to a file."""


args_list = []

for arg in sys.argv[1:]:
    args_list.append(arg)

save_to_json_file(args_list, "add_item.json")

loaded_list = load_from_json_file("add_item.json")
print(loaded_list)
