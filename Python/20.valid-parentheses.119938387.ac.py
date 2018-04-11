#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (33.99%)
# Total Accepted:    322.8K
# Total Submissions: 949.6K
# Testcase Example:  '"["'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        corresponding = {"(":")", "[":"]", "{":"}"}
        stack = []
        for cc in s:
            if cc in {"(", "[", "{"}:
                stack.append(cc)
            else:
                if (len(stack) == 0 or corresponding[stack.pop()] != cc):
                    return False
        return len(stack) == 0
