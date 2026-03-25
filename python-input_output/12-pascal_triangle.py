#!/usr/bin/python3
"""Defines a Pascal Triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the triangle."""
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) < n:
        prev = tri[-1]
        row = [1]
        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i + 1])
        row.append(1)
        tri.append(row)
    return tri
