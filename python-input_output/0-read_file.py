#!/usr/bin/python3
"""
This module contains a function that reads a text file (UTF-8)
and prints its contents to standard output.
"""

def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    This function uses the 'with' statement to ensure that the file
    is automatically closed after its suite finishes.

    Args:
        filename (str): The name of the file to be read. Defaults to "".
    """
    # The 'with' statement handles opening the file and guarantees it will be
    # closed automatically, even if errors occur.
    # 'encoding="utf-8"' is specified to correctly handle a wide range of
    # text characters.
    with open(filename, 'r', encoding="utf-8") as f:
        # f.read() reads the entire content of the file into a single string.
        # print() then outputs that string to the console.
        # 'end=""' prevents the print function from adding an extra newline
        # at the end, so the output exactly matches the file content.
        print(f.read(), end="")

if __name__ == "__main__":
    # This block demonstrates how to use the function.
    # For this to work, you must first create a file named 'my_file.txt'
    # in the same directory with some text content inside it.

    # Example:
    # Create a file named my_file.txt with the following content:
    #
    # Hello, this is a test file.
    # It has multiple lines.
    # Python is fun!

    print("--- Reading from my_file.txt ---")
    read_file("my_file.txt")
    print("--- End of file ---")

