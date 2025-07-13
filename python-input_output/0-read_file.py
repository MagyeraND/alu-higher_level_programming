#!/usr/bin/python3
"""
This module contains a function that reads a text file (UTF-8)
and prints its contents to standard output.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    print("--- Reading from my_file.txt ---")
    read_file("my_file.txt")
    print("--- End of file ---")

