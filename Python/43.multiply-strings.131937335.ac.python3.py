#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (28.01%)
# Total Accepted:    135.6K
# Total Submissions: 484.1K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0]* (len(num1) + len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                res[i+j] += int(e1) * int(e2)
                res[i+j+1] += res[i+j] // 10
                res[i+j] %= 10
    
        while len(res) > 1 and res[-1] == 0: 
            res.pop()
        return ''.join( map(str,res[::-1]) )
