#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (36.42%)
# Total Accepted:    44.5K
# Total Submissions: 122.1K
# Testcase Example:  '5'
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# ⁠
# Given n, find the total number of full staircase rows that can be formed.
# 
# n is a non-negative integer and fits within the range of a 32-bit signed
# integer.
# 
# Example 1:
# 
# n = 5
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# 
# Because the 3rd row is incomplete, we return 2.
# 
# 
# 
# Example 2:
# 
# n = 8
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# 
# Because the 4th row is incomplete, we return 3.
# 
# 
#
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        guess = int((2 * n) ** 0.5)
        if (guess + 1) * guess <=  2 * n:
            return guess
        elif guess * (guess - 1) <=  2 * n:
            return guess - 1
        else:
            return guess - 2
