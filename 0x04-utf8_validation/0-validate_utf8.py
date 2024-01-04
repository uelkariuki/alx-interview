#!/usr/bin/python3

"""UTF-8 Validation"""


def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding
    """
    no_of_bytes = 0

    for value in data:
        if no_of_bytes > 0:
            if value >> 6 != 0b10:
                return False
            # subtract as we processed one of the
            # continuation bytes
            no_of_bytes -= 1
        else:
            if value >> 7 == 0:
                # set as 0 as its single-byte character
                no_of_bytes = 0
            # check first 3 bits if 110, its 2-byte character
            elif value >> 5 == 0b110:
                no_of_bytes = 1
            elif value >> 4 == 0b1110:
                # expecting 2 more bytes for this character
                no_of_bytes = 2
            elif value >> 3 == 0b11110:
                no_of_bytes = 3
            else:
                # the first bits don't match any valid utf-8 character start
                return False
        return no_of_bytes == 0
