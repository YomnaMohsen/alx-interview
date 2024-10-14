#!/usr/bin/python3
"""Min operations module"""


def minOperations(n):
    """a method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    Args:
    n: number of chars in file after operations.
    return:
    int: no of operations.
    """
    if n <= 1:
        return 0

    num_op = 0
    div_factor = 2

    while n > 1:
        while n % div_factor == 0:
            num_op += div_factor
            n //= div_factor
        div_factor += 1

    return num_op
