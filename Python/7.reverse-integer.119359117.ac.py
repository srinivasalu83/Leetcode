#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.37%)
# Total Accepted:    393.9K
# Total Submissions: 1.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# Input: 123
# Output:  321
# 
# 
# 
# Example 2:
# 
# Input: -123
# Output: -321
# 
# 
# 
# Example 3:
# 
# Input: 120
# Output: 21
# 
# 
# 
# Note:
# Assume we are dealing with an environment which could only hold integers
# within the 32-bit signed integer range. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.
# 
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0
        while x != 0:
            result = result * 10 + x % 10
            x = int(x / 10)
        result = result * sign
        if (result > 2147483647 or result < -2147483648):
            return 0
        return result
    
