#!/usr/bin/python3
"""Pascal triangle module"""
from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """Fn to generate pascal traingle
    Args:
    n: no of rows
    return list of list of int
    """
    res = [[1]]
    if n == 0:
        return [[]]
    elif n == 1:
        return res
    
    for i in range((n-1)):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res
