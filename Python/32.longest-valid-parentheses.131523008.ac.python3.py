#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (23.19%)
# Total Accepted:    123.5K
# Total Submissions: 532.4K
# Testcase Example:  '""'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# 
# For "(()", the longest valid parentheses substring is "()", which has length
# = 2.
# 
# 
# Another example is ")()())", where the longest valid parentheses substring is
# "()()", which has length = 4.
# 
#
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen, longest = len(s), 0
        stack = []
        for i in range(sLen):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) != 0:
                    if s[stack[-1]] == '(':
                         stack.pop()
                    else:
                         stack.append(i)
                else:
                    stack.append(i)
        if len(stack) == 0:
            return sLen
        a, b = sLen, 0
        while len(stack) != 0:
            b = stack.pop()
            longest = max(longest, a - b - 1)
            a = b
        longest = max(longest, a)
        return longest
                         
