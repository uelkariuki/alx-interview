#!/usr/bin/python3

"""UTF-8 Validation"""

from typing import List

def validUTF8(data: List[int]) -> bool:
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding
    """
    no_of_bytes = 0

    for value in data:
        if no_of_bytes == 0:
            # check first 3 bits if 110, its 2-byte character
            if (value >> 5) == 0b110:
                no_of_bytes = 1
            elif (value >> 4) == 0b1110:
                # expecting 2 more bytes for this character
                no_of_bytes = 2
            elif (value >> 3) == 0b11110:
                no_of_bytes = 3
            elif (value >> 7) == 0:
                continue
            else:
                return False
        else:
            if (value >> 6) != 0b10:
                return False
            # subtract as we processed one of the
            # continuation bytes
            no_of_bytes -= 1
    return no_of_bytes == 0
