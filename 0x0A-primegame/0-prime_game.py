#!/usr/bin/python3
"""prime game module"""


def isWinner(x, nums):
    """args:
    x:no of rounds
    nums: array of ints of size x
    return name of winner or none
    """

    maria = False
    ben = False

    def SieveOfEratosthenes(n):
        """fine prime numbers in list up to n"""
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if prime[p]:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        prime[0] = False
        prime[1] = False
        return prime

    max_num = max(nums)
    prime_list = SieveOfEratosthenes(max_num)

    for round in nums:
        round_list = [i for i in range(round + 1) if prime_list[i]]
        if (len(round_list) % 2 == 0):
            ben = True
            maria = False
        else:
            maria = True
            ben = False
    if maria:
        return "Maria"
    if ben:
        return "Ben"
    return None
