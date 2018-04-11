#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (47.48%)
# Total Accepted:    209K
# Total Submissions: 440.2K
# Testcase Example:  '""\n""'
#
# Given two strings s and t, write a function to determine if t is an anagram
# of s. 
# 
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        for c in t:
            chars[c] = chars.get(c, 0) - 1
            if chars[c] < 0:
                return False
        for c in chars:
            if chars[c] != 0:
                return False
        return True
