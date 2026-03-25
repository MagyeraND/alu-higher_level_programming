#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after each of these characters: . ? and :.
    There should be no space at the beginning or at the end of each line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = (char + "\n\n").join([line.strip(" ")
                                     for line in text.split(char)])
    print(text, end="")
