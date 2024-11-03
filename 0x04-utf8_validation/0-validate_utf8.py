#!/usr/bin/python3
"""UTF8 validation module"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """validates utf8 encoding"""
    n_bytes = 0
    for value in data:
        if n_bytes > 0:
            if value >> 6 != 0b10:
                return False
            num_of_bytes -= 1
        else:
            if value >> 7 == 0:
                num_of_bytes = 0
            elif value >> 5 == 0b110:
                num_of_bytes = 1
            elif value >> 4 == 0b1110:
                num_of_bytes = 2
            elif value >> 3 == 0b11110:
                num_of_bytes = 3
            else:
                return False
        return num_of_bytes == 0
