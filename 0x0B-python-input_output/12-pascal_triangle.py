#!/usr/bin/python3
"""
Module: 12-pascal_triangle
Contains the definition of the pascal_triangle function.
"""

def pascal_triangle(n):
    """
    Generates the Pascal's triangle of size n.

    Args:
        n (int): The size of the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]
    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(triangle[x-1][y-1] + triangle[x-1][y])
        row.append(1)
        triangle.append(row)

    return triangle
