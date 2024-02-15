#!/usr/bin/python3

"""
Prime game
"""


def isWinner(x, nums):
    """
    Args:
    x: the number of rounds
    nums: an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    if not isinstance(x, int) or not isinstance(nums, list) or x < 1:
        return 
    def SieveofEratosthenes(n):
        """ Returns prime numbers found upto given limit
        """
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):
            # if prime[p] is not changed then it is prime
            if prime[p] is True:
                # update all multiples of p
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        # return the prime numbers

        return [p for p in range(2, n + 1) if prime[p]]

    def play_game(n):
        """
        Simulates the game
        """
        primes = SieveofEratosthenes(n)
        return 'Maria' if len(primes) % 2 == 1 else 'Ben'

    scores = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = play_game(n)
        scores[winner] += 1

    if scores['Maria'] > scores['Ben']:
        return "Maria"
    elif scores['Ben'] > scores['Maria']:
        return "Ben"
    else:
        return None
