#!/usr/bin/python3

"""
Given a pile of coins of different values, determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """
    # greedy approach
    coinCount = 0
    coins.sort(reverse=True)

    if total <= 0 or any(i <= 0 for i in coins):
        return 0

    for coin in coins:
        while total >= coin:
            coinCount += 1
            total -= coin

    if total == 0:
        return coinCount
    return -1
