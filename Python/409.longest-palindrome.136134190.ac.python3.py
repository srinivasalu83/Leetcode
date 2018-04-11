#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (45.94%)
# Total Accepted:    62.6K
# Total Submissions: 136.3K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        if_contain_single = False
        res = 0
        for c, count in chars.items():
            if count % 2 == 1:
                if_contain_single = True
            res += count // 2 * 2
        return res + 1 if if_contain_single else res
