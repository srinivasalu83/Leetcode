#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.29%)
# Total Accepted:    306.2K
# Total Submissions: 1.2M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example:
# 
# 
# Input: "babad"
# 
# Output: "bab"
# 
# Note: "aba" is also a valid answer.
# 
# 
# 
# 
# Example:
# 
# 
# Input: "cbbd"
# 
# Output: "bb"
# 
# 
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Manacher algorithm
        sp = '*' + '*'.join(s) + '*'
        rightmost = 0
        piv = 0
        record = []
        pivresult = 0
        largest = 0
        for ii in range(len(sp)):
            if ii >= rightmost:
                ratio = 1
            else:
                ratio = min(record[2 * piv - ii], rightmost - ii + 1)
            while (ii + ratio < len(sp) and ii + 1 > ratio 
                and sp[ii + ratio] == sp[ii - ratio]):
                ratio = ratio + 1
            record.append(ratio)
            if (ii + ratio - 1) > rightmost: # update
                rightmost = ii + ratio - 1
                piv = ii
            if ratio > largest: # mark
                pivresult = ii
                largest = ratio
        return sp[pivresult - record[pivresult] + 1:
                  pivresult + record[pivresult]].replace('*', '')
