#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (48.02%)
# Total Accepted:    205.4K
# Total Submissions: 427.7K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def recurssivefind(temp, m, bal):
            #print(temp, m, bal)
            res = []
            if (bal < 0 or bal > n): #invalid
                return []
            if (m == 0 and bal == 0):
                #print("_______________"+temp)
                return [temp]
            elif (m != 0):
                res = res + recurssivefind(temp+'(', m-1, bal+1)
                res = res + recurssivefind(temp+')', m-1, bal-1)
            return res
        return recurssivefind("", 2 * n, 0)
