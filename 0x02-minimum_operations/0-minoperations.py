#!/usr/bin/python3
"""
Script for miniOperations
"""


def minOperations(n: int) -> int:
    """
    Gets the fewest number of operations needed
    to result in exactly n H characters
    """
    if (n < 2):
        return 0
    op, root = 0, 2
    while root <= n:
        if n % root == 0:
            op += root
            n = n / root
            root -= 1
        root += 1
    return op
