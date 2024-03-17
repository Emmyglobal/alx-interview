#!/usr/bin/python3
"""This Script solves the pascal principle"""


def factorial(num):
    """ Factorial Function """
    if num == 0:
        return 1
    return num * factorial(num - 1)


def pascal_triangle(n):
    """ Pascal function """
    triangle = []  # Initialize the triangle list
    if n <= 0:
        return triangle  # Return an empty list for invalid inputs
    for x in range(n):
        temp = []
        for y in range(x + 1):
            value = factorial(x) // (factorial(y) * factorial(x - y))
            temp.append(value)
        triangle.append(temp)
    return triangle  # Return the Pascal's triangle list


def print_triangle(triangle):
    """Prints the Pascal's triangle"""
    for row in triangle:
        print(row)
