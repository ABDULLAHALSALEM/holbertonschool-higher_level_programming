#!/usr/bin/python3
"""Module that provides a function to add two integers.

The function add_integer takes two numbers (integers or floats)
and returns their integer sum.
"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98

    Returns:
        int: the addition of a and b

    Raises:
        TypeError: if a is not an integer or float
        TypeError: if b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
