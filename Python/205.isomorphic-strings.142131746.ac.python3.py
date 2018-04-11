#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (34.74%)
# Total Accepted:    134.2K
# Total Submissions: 386.3K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# For example,
# Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.
# 
# Note:
# You may assume both s and t have the same length.
#
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapping = dict()
        out_field = set()
        for c1, c2 in zip(s, t):
            if c1 in mapping and mapping[c1] == c2:
                continue
            elif c1 not in mapping and c2 not in out_field:
                mapping[c1] = c2
                out_field.add(c2)
            else:
                return False
        return True
