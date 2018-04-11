#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (36.98%)
# Total Accepted:    115.2K
# Total Submissions: 311.4K
# Testcase Example:  '0'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
from math import log
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
