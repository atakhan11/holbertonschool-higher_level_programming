#!/usr/bin/python3
"""This Module is for dividing elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals"""

    # Empty matrix case
    if matrix == []:
        return []

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all elements are int or float
    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix with divided elements
    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]

    return new_matrix
