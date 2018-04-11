#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (32.22%)
# Total Accepted:    82.3K
# Total Submissions: 255.4K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
# 
# Here is an example:
# S = "rabbbit", T = "rabbit"
# 
# Return 3.
# 
#
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        self.mem = {}
        if not t:
            return 1
        if not s:
            return 0   
        mapping = {}
        for i, c1 in enumerate(t):
            for j, c2 in enumerate(s):
                if c1 == c2:
                    mapping.setdefault(i, []).append(j)
        print(mapping)
        if not mapping:
            return 0
        return self.recursive_count(mapping, 0, -1)
    
    def recursive_count(self, mapping, i, j):
        if (i, j) in self.mem:
            return self.mem[(i, j)]
        if i == len(mapping) - 1:
            res = sum(map(lambda x: x > j, mapping[i]))
            # print(i, j, res)
            self.mem[(i, j)] = res
            return res
        else:
            res = 0
            for t in mapping[i]:
                if t > j:
                    res += self.recursive_count(mapping, i + 1, t)
            # print(i, j, res)
            self.mem[(i, j)] = res
            return res
