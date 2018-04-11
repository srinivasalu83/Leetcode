#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (20.31%)
# Total Accepted:    168.2K
# Total Submissions: 828.1K
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given an encoded message containing digits, determine the total number of
# ways to decode it.
# 
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# 
# The number of ways decoding "12" is 2.
# 
#
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        for i in range(n):
            if s[i] > '9' or s[i] < '0':
                return 0
        ways = [0 for i in range(n + 1)]
        ways[-1] = 1
        if '9' >= s[-1] >= '1':
            ways[-2] = 1
        for i in reversed(range(n - 1)):
            if 10 <= int(s[i: i + 2]) <= 26:
                ways[i] += ways[i + 2]
            if '9' >= s[i] >= '1':
                ways[i] += ways[i + 1]
        print(ways)
        return ways[0]
