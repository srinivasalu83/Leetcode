#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (47.09%)
# Total Accepted:    116.7K
# Total Submissions: 247.9K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = {}
        for c in s:
            res[c] = res.get(c, 0) + 1
        for i, c in enumerate(s):
            if res[c] == 1:
                return i
        return -1
