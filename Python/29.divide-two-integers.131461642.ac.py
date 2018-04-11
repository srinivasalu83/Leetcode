#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (15.72%)
# Total Accepted:    130.4K
# Total Submissions: 829.1K
# Testcase Example:  '0\n1'
#
# 
# Divide two integers without using multiplication, division and mod
# operator.
# 
# 
# If it is overflow, return MAX_INT.
# 
#
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        else:
            sign = 1
        dividend, divisor = abs(dividend), abs(divisor)
        ret = 0
        while dividend >= divisor:
            temp, i = divisor, 1 # temp是divisor的倍数，倍数用i表示
            while dividend >= temp:
                dividend -= temp
                ret += i
                i <<= 1
                temp <<= 1
        return min(max(-2147483648, sign * ret), 2147483647)
