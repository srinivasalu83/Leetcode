#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (14.08%)
# Total Accepted:    224.7K
# Total Submissions: 1.6M
# Testcase Example:  '""'
#
# Implement atoi to convert a string to an integer.
# 
# Hint: Carefully consider all possible input cases. If you want a challenge,
# please do not see below and ask yourself what are the possible input cases.
# 
# Notes: It is intended for this problem to be specified vaguely (ie, no given
# input specs). You are responsible to gather all the input requirements up
# front.
# 
# 
# 
# Requirements for atoi:
# 
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
# 
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned. If the
# correct value is out of the range of representable values, INT_MAX
# (2147483647) or INT_MIN (-2147483648) is returned.
# 
#
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ii = 0
        while (ii < len(str)):
            if str[ii] != ' ':
                break
            ii = ii + 1
        if ii == len(str):
            return 0
        sign = 1
        if (str[ii] == '+'):
            ii = ii + 1
        elif (str[ii] == '-'):
            ii = ii + 1
            sign = -1
        elif (str[ii] > '9' or str[ii] < '0'):
            return 0
        result = 0
        while (ii < len(str)):
            if (str[ii] > '9' or str[ii] < '0'):
                break
            result = result * 10 + ord(str[ii]) - ord('0')
            ii = ii + 1
        result = result * sign
        result = 2147483647 if result > 2147483647 else result
        result = -2147483648 if result < -2147483648 else result
        return result
