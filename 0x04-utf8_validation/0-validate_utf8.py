#!/usr/bin/python3

"""UTF-8 Validation"""


def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding
    """

    def check(num):
        """Function that returns the count of 1s"""
        mask = 1 << (8-1) # 10000000
        i = 0
        while num & mask:
            mask >>= 1
            i += 1
        return i

    i = 0
    while i < len(data):
        # j is the current utf-8 character
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        # invalid utf-8 encoding
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            current = check(data[i])
            
            if current != 1:
                return False
            i += 1
        return True


