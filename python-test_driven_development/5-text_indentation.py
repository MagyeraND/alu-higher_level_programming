#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Indents text after . ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for char in ".?:":
        text = (char + "\n\n").join([line.strip(" ") for line in text.split(char)])
    print(text, end="")
