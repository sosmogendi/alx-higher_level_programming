#!/usr/bin/python3
"""Module to multiply two matrices
"""


def matrix_mul(m_a, m_b):
    """Function to multiply two matrices and return the result
    """
    # Validate m_a and m_b
    validate_matrices(m_a, m_b)
    
    # Get the dimensions of the matrices
    rows_a = len(m_a)
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    cols_b = len(m_b[0])
    
    # Check if the matrices can be multiplied
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Initialize the result matrix
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    # Perform matrix multiplication
    for x in range(rows_a):
        for y in range(cols_b):
            for z in range(cols_a):
                result[x][y] += m_a[x][z] * m_b[z][y]
    
    return result


def validate_matrices(m_a, m_b):
    """Function to validate the matrices before multiplication
    """
    # Validate m_a
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    
    # Validate m_b
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

