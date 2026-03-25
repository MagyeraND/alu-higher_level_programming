#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after each ., ? and :.
    Leading/trailing spaces in each line are removed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = [".", "?", ":"]
    for c in chars:
        text = (c + "\n\n").join([line.strip(" ") for line in text.split(c)])
    print(text, end="")
