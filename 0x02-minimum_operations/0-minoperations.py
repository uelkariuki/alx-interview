#!/usr/bin/python3

"""
In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste. Given a number
n, write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.

Example:
n = 9
H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH
=> Paste => HHHHHHHHH
Number of operations: 6
"""


def minOperations(n):
    """Returns an integer"""
    if n <= 1:
        return 0

    divisor = 2
    min_no_Operations = 0

    while n > 1:
        if n % divisor == 0:
            n = n / divisor
            min_no_Operations = min_no_Operations + divisor

        else:
            divisor += 1

    return min_no_Operations
