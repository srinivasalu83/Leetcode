#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (24.85%)
# Total Accepted:    80.7K
# Total Submissions: 324.8K
# Testcase Example:  '"aab"'
#
# 
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# 
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using
# 1 cut.
# 
#
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        opt = [i - 1 for i in range(n + 1)]
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                opt[i + j + 1] = min(opt[i + j + 1], 1 + opt[i - j])
                j += 1
            j = 1
            while i - j + 1 >= 0 and i + j < n and s[i - j + 1] == s[i + j]:
                opt[i + j + 1] = min(opt[i + j + 1], 1 + opt[i - j + 1])
                j += 1
        print(opt)
        return opt[-1]
    
