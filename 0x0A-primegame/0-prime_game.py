#!/usr/bin/python3
"""prime game module"""


def isWinner(x, nums):
    """args:
    x:no of rounds
    nums: array of ints of size x
    return name of winner or none
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria = 0
    ben = 0

    def SieveOfEratosthenes(n):
        """find prime numbers in list up to n"""
        prime = [True for i in range(n+1)]
        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        prime[0] = False
        prime[1] = False
        return prime

    max_num = max(nums)
    prime_list = SieveOfEratosthenes(max_num)

    for j in range(x):
   # for round in nums:
        round_list = [i for i in range(nums[j] + 1) if prime_list[i]]
        if len(round_list) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    return None
