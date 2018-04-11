#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (48.04%)
# Total Accepted:    223.4K
# Total Submissions: 465K
# Testcase Example:  '"DCXXI"'
#
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = '*' + s + '*'
        mapping = {'*': 0, 'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for ii in range(len(s) - 1, 0, -1):
            latter = s[ii]
            former = s[ii-1]
            if (mapping[former] >= mapping[latter]):
                result = result + mapping[former]
            else:
                result = result - mapping[former]
            print(result, ii, mapping[former], mapping[latter])
        return result
