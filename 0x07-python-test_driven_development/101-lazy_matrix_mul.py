#!/usr/bin/python3
"""Module to multiply two matrices using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function to multiply two matrices using NumPy and return the result
    """
    # Convert the input matrices to NumPy arrays
    np_a = np.array(m_a)
    np_b = np.array(m_b)
    
    # Perform matrix multiplication using NumPy's dot function
    final = np.dot(np_a, np_b)
    
    return final.tolist()
