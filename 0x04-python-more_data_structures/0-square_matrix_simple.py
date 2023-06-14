#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        n_row = [w**2 for w in row]
        new_matrix.append(n_row)
    return new_matrix
