#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (40.73%)
# Total Accepted:    169.1K
# Total Submissions: 415.1K
# Testcase Example:  '1'
#
# 
# Given an integer, write a function to determine if it is a power of two.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n != 0 and n & (n - 1) == 0
