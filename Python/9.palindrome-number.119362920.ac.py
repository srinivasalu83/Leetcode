#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (35.77%)
# Total Accepted:    319.3K
# Total Submissions: 892.7K
# Testcase Example:  '-2147483648'
#
# Determine whether an integer is a palindrome. Do this without extra space.
# 
# click to show spoilers.
# 
# Some hints:
# 
# Could negative integers be palindromes? (ie, -1)
# 
# If you are thinking of converting the integer to string, note the restriction
# of using extra space.
# 
# You could also try reversing an integer. However, if you have solved the
# problem "Reverse Integer", you know that the reversed integer might overflow.
# How would you handle such case?
# 
# There is a more generic way of solving this problem.
# 
# 
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def getnum(x, exp):
            """
            (123, 1) -> 3
            (123, 2) -> 2
            (123, 3) -> 1
            """
            return int(x / 10**(exp - 1)) % 10
        if (x == 0):
            return True
        if (x < 0):
            return False
        from math import log10
        total = int(log10(x)) + 1
        for ii in range(1, int(total / 2) + 1):
            if (getnum(x, ii) != getnum(x, total - ii + 1)):
                return False
        return True
