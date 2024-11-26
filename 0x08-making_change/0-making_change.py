#!/usr/bin/python3
"""Making change module"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Calculates fewest number of coins
    needed to meet a given amount total"""
    if total <= 0:
        return 0
    target, steps = 0, 0
    coins.sort(reverse=True)

    for c in coins:
        if target < total:
            target += c
            steps += 1

        if target == total:
            return steps

        else:
            target -= c
            steps -= 1
    return -1
