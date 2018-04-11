#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (39.73%)
# Total Accepted:    235.2K
# Total Submissions: 592K
# Testcase Example:  '[0]'
#
# Given a non-negative integer represented as a non-empty array of digits, plus
# one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
#
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        ret, c = [], 1
        for i, v in enumerate(digits):
            v = v + c
            c = v // 10
            ret.append(v % 10)
        if c != 0:
            ret.append(c)
        ret.reverse()
        return ret
    
