#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (35.84%)
# Total Accepted:    66.9K
# Total Submissions: 186.6K
# Testcase Example:  '"()())()"'
#
# 
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
# 
# Note: The input string may contain letters other than the parentheses ( and
# ). 
# 
# 
# 
# Examples:
# 
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]
# 
# 
# 
# Credits:Special thanks to @hpplayer for adding this problem and creating all
# test cases.
#
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = set([])
        self.remove(s, 0, ('(', ')'), result)
        return list(result)
    
    def remove(self, s, start, par, result):
        count = 0
        for i in range(start, len(s)):
            count += (s[i] == par[0]) - (s[i] == par[1])
            if count >= 0:
                continue
            for j in range(i + 1):
                if s[j] == par[1]:
                    self.remove(s[:j] + s[j + 1:], i, par, result)
            return
        reversed_s = s[::-1]
        if par[0] == '(':
            # we already have #( >= #), we also need to check #( <= #)
            self.remove(reversed_s, 0, (')', '('), result) 
        else:
            result.add(reversed_s)
