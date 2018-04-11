#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (43.90%)
# Total Accepted:    27.2K
# Total Submissions: 62K
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
# 
# Example 1:
# 
# Input: 100
# Output: "202"
# 
# 
# 
# Example 2:
# 
# Input: -7
# Output: "-10"
# 
# 
# 
# Note:
# The input will be in range of [-1e7, 1e7].
# 
#
from math import log

class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        res = [] if num >= 0 else ['-']
        num = abs(num)
        base = int(log(num, 7))
        while base >= 0:
            tmp = 7 ** base
            res.append(str(num // tmp))
            num %= tmp
            base -= 1
        return ''.join(res)
            
