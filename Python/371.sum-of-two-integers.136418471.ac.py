#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.89%)
# Total Accepted:    95K
# Total Submissions: 186.7K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# Example:
# Given a = 1 and b = 2, return 3.
# 
# 
# Credits:Special thanks to @fujiaozhu for adding this problem and creating all
# test cases.
#
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            print(a, b)
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
