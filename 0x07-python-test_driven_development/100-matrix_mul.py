#!/usr/bin/python3
"""
This is the "100-matrix_mul" module.
The 100-matrix_mul module supplies one function, matrix_mul(m_a, m_b).
"""


def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a cannot be empty")
    if len(m_b) == 0:
        raise ValueError("m_b cannot be empty")
    sizeA = None
    sizeB = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_a cannot be empty")
        if sizeA is None:
            sizeA = len(i)
        if sizeA != len(i):
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for a in m_b:
        if type(a) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(a) == 0:
            raise ValueError("m_b cannot be empty")
        if sizeB is None:
            sizeB = len(a)
        if sizeB != len(a):
            raise TypeError("each row of m_b must be of the same size")
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len(i) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for y in range(len(m_a)):
        nMatrix = []
        for j in range(len(a)):
            n = 0
            for k in range(len(i)):
                n += m_a[y][k] * m_b[k][j]
            nMatrix.append(n)
        matrix.append(nMatrix)
    return matrix
