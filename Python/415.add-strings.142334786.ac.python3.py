#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (41.78%)
# Total Accepted:    55.2K
# Total Submissions: 132K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        num1 = list(reversed([int(digit) for digit in num1])) + [0]
        num2 = list(reversed([int(digit) for digit in num2])) + [0] * (len(num1) - len(num2))
        summ = [i + j for i, j in zip(num1, num2)]
        for i in range(len(summ) - 1):
            if summ[i] >= 10:
                summ[i + 1] += 1
                summ[i] %= 10
        result = ''.join(reversed([str(i) for i in summ])).lstrip('0')
        return '0' if not result else result
        
        
