#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (26.50%)
# Total Accepted:    152.1K
# Total Submissions: 573.9K
# Testcase Example:  '0'
#
# Description:
# Count the number of prime numbers less than a non-negative number, n.
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
from math import sqrt, ceil

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
