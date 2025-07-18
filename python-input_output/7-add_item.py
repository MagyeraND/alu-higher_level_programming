#!/usr/bin/python3
import sys
import os.path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list or start fresh
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command-line arguments (excluding script name itself)
my_list.extend(sys.argv[1:])

# Save updated list
save_to_json_file(my_list, filename)

