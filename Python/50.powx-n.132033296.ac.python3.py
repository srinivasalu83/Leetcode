#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (26.03%)
# Total Accepted:    207.6K
# Total Submissions: 797.5K
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n).
# 
# 
# 
# 
# Example 1:
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# 
# Example 2:
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
#
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0:
            return 0
        sign = n > 0
        n, p, mul, ret = abs(n), 1, x, 1
        while n > 0:
            print(p, mul, ret, n)
            if p * 2 <= n:
                mul *= mul
                p *= 2
            else:
                ret *= mul
                n -= p
                p, mul = 1, x
        if sign:
            return ret
        else:
            return 1 / ret
