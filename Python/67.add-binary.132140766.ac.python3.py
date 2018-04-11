#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (34.02%)
# Total Accepted:    196.7K
# Total Submissions: 578.1K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# For example,
# a = "11"
# b = "1"
# Return "100".
# 
#
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = [int(c) for c in a]
        b = [int(c) for c in b]
        if len(a) < len(b):
            a, b = b, a
        for i in range(1, len(b) + 1):
            a[-i] = a[-i] + b[-i]
        c = 0
        for i in reversed(range(len(a))):
            a[i] = a[i] + c
            c = a[i] // 2
            a[i] = a[i] % 2
        if c != 0:
            a.insert(0, c)
        return ''.join([str(i) for i in a])
