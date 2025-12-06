#!/usr/bin/python3
"""Module for matrix division.

This module provides the matrix_divided function
which divides all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix: list of lists of integers/floats.
        div: number (int or float).

    Returns:
        A new matrix with each value divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If each row of the matrix doesn't have same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """

    # Check matrix
    if (not isinstance(matrix, list) or
            len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if row_len == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Produce new matrix
    new_matrix = []
    for row in matrix:
        new_matrix.append([round(x / div, 2) for x in row])

    return new_matrix
