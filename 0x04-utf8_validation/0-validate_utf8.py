#!/usr/bin/python3

"""UTF-8 Validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding
    """

    def countOne(num):
        """Method to count number of ones"""
        count = 0
        for i in range(7, -1, -1):
            if num & (1 << i):
                count += 1
            else:
                break
        return count
    count = 0
    for x in data:
        if not count:
            count = countOne(x)
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
            count -= 1
        else:
            count -= 1
            if countOne(x) != 1:
                return False
    return count == 0
