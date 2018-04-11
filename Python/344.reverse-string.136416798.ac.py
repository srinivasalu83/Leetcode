#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (60.32%)
# Total Accepted:    237K
# Total Submissions: 393K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and returns the string
# reversed.
# 
# 
# Example:
# Given s = "hello", return "olleh".
# 
#
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
