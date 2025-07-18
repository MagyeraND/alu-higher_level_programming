#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object created from the JSON file content.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)







