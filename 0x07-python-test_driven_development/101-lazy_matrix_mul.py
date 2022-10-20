#!/usr/bin/python3
"""
    Module to find the max integer in a list
    Write a function that multiplies 2 matrices by using
    the module NumPy
    To install it: pip3 install numpy==1.15.0
    Prototype: def lazy_matrix_mul(m_a, m_b):
    Test cases should be the same as 100-matrix_mul
    but with new exception type/message
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
