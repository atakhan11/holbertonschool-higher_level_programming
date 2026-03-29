#!/usr/bin/python3
"""This Module containing print_square function"""


def print_square(size):
    """Function to print a square"""

    # Checking if size not integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Checking if size less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print(size * "#")
