#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (36.69%)
# Total Accepted:    71.2K
# Total Submissions: 194K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows: 
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or
# lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results
# (-1, 1, or 0):
# 
# -1 : My number is lower
# ⁠1 : My number is higher
# ⁠0 : Congrats! You got it!
# 
# 
# Example:
# 
# n = 10, I pick 6.
# 
# Return 6.
# 
# 
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start < end:
            mid = int((start + end) / 2)
            g = guess(mid)
            if g == 0:
                return mid
            elif g == 1:
                start = mid + 1
            else:
                end = mid - 1
        return start
