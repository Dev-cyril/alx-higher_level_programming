#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(list(map(lambda x: x * x, i)) for i in matrix)
    return new_matrix
