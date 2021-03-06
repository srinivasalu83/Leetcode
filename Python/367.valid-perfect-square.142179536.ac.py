#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (38.68%)
# Total Accepted:    69.7K
# Total Submissions: 180.3K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# 
# Input: 16
# Returns: True
# 
# 
# 
# Example 2:
# 
# Input: 14
# Returns: False
# 
# 
# 
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
