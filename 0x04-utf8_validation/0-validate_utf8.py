#!/usr/bin/python3
"""UTF8 validation module"""
from typing import List


def validUTF8(self, data: List[int]) -> bool:
        # number of bytes to process
        num_of_bytes = 0

        # Loop through each integer in the data list
        for value in data:
            # If we're in the middle of parsing a valid UTF-8 character
            if num_of_bytes > 0:
                # Check if the first 2 bits are 10, which is a continuation byte
                if value >> 6 != 0b10:
                    # Not a continuation byte, so the sequence is invalid
                    return False
                # We've processed one of the continuation bytes
                num_of_bytes -= 1
            # If we're at the start of a UTF-8 character
            else:
                # Check the first bit; if it's 0, we have a 1-byte character
                if value >> 7 == 0:
                    # Set to 0 as it's a single-byte character
                    num_of_bytes = 0
                # Check the first 3 bits; if they're 110, it's a 2-byte character
                elif value >> 5 == 0b110:
                    # Expecting one more byte for this character
                    num_of_bytes = 1
                # Check the first 4 bits; if they're 1110, it's a 3-byte character
                elif value >> 4 == 0b1110:
                    # Expecting two more bytes for this character
                    num_of_bytes = 2
                # Check the first 5 bits; if they're 11110, it's a 4-byte character
                elif value >> 3 == 0b11110:
                    # Expecting three more bytes for this character
                    num_of_bytes = 3
                else:
                    # The first bits do not match any valid UTF-8 character start
                    return False