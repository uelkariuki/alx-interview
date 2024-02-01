#!/usr/bin/python3

"""
Given a pile of coins of different values, determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """
    # default value for total is total + 1
    # * (total + 1) 0...total
    if total == 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for t in range(1, total + 1):
        for coin in coins:
            if t - coin >= 0:
                dp[t] = min(dp[t], 1 + dp[t - coin])

    if dp[total] != total + 1:
        return dp[total]
    else:
        return -1
