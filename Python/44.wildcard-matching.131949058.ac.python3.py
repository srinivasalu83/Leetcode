#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (21.00%)
# Total Accepted:    121.7K
# Total Submissions: 579.7K
# Testcase Example:  '"aa"\n"a"'
#
# Implement wildcard pattern matching with support for '?' and '*'.
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
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
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false
# 
#
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sP, pP, matchS, starP = 0, 0, 0, -1
        while sP < len(s):
            if pP < len(p) and (p[pP] == '?' or s[sP] == p[pP]):
                pP += 1
                sP += 1
            elif pP < len(p) and p[pP] == '*': # recover point
                starP = pP
                matchS = sP
                pP += 1
            elif starP != -1: # go back!
                pP = starP + 1
                matchS += 1
                sP = matchS
            else:
                return False
        while pP < len(p) and p[pP] == '*':
            pP += 1
        return pP == len(p)
        
