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
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for t in range(coin, total + 1):
            dp[t] = min(dp[t], 1 + dp[t - coin])

    if dp[total] != float('inf'):
        return dp[total]
    else:
        return -1
