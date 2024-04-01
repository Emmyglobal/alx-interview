#!/usr/bin/python3
"""
Minimum Ops
a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Minimum Ops
    """
    if n == 1:
        return 0

    op = 0
    h = 1
    while h < n:
        if n % h == 0:
            h_dup = h
            op += 1
        h += h_dup
        op += 1

    if h == n:
        return op
    else:
        return 0
