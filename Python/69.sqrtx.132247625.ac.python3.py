#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (28.87%)
# Total Accepted:    224.4K
# Total Submissions: 777.3K
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x.
# 
# x is guaranteed to be a non-negative integer.
# 
# 
# 
# Example 1:
# 
# Input: 4
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we want to return
# an integer, the decimal part will be truncated.
# 
# 
#
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Newton: new_x = (x + a / x) / 2
        if x == 0:
            return 0
        r = x
        new_r = (r + x / r) / 2
        while abs(new_r - r) >= 0.5:
            new_r, r = (new_r + x / new_r) / 2, new_r
        return int(new_r)
