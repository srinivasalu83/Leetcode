#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (35.67%)
# Total Accepted:    118.9K
# Total Submissions: 333.3K
# Testcase Example:  '"aab"'
#
# 
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# 
# Return all possible palindrome partitioning of s.
# 
# 
# For example, given s = "aab",
# 
# Return
# 
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ispal = self.ispal
        res = [[s]] if ispal(s) else []
        for i in range(1, len(s)):
            if ispal(s[i:]):
                sub_res = self.partition(s[:i])
                for r in sub_res:
                    r.append(s[i:])
                res += sub_res
        return res
                    
    
    def ispal(self, s):
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
        
