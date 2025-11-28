#!/usr/bin/python3
"""Module that defines a Pascal's triangle function."""


def pascal_triangle(n):
    """Return a list of lists of integers representing the Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Each row starts and ends with 1
        row = [1]
        # Each inner element is sum of two elements above it
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
