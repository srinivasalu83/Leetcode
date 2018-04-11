#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (24.34%)
# Total Accepted:    193.6K
# Total Submissions: 795.3K
# Testcase Example:  '"aa"\n"a"'
#
# Implement regular expression matching with support for '.' and '*'.
# 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# The matching should cover the entire input string (not partial).
# 
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
# 
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true
# 
#
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        firstmatch = bool(s) and p[0] in {'.', s[0]}
        if (len(p) >= 2 and p[1] == '*'):
            return self.isMatch(s, p[2:]) or (firstmatch and self.isMatch(s[1:], p))
        else:
            return firstmatch and self.isMatch(s[1:], p[1:])

