#!/usr/bin/python3
"""Module for integer addition."""


def add_integer(a, b=98):
    """Adds two integers. Floats are cast to integers.
    Raises TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
