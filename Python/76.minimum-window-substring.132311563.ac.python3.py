#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (26.77%)
# Total Accepted:    144.3K
# Total Submissions: 538.9K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# 
# Minimum window is "BANC".
# 
# Note:
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# 
# If there are multiple such windows, you are guaranteed that there will always
# be only one unique minimum window in S.
# 
#
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        lo, hi, end = 0, 0, len(s)
        res_lo, res_hi = 0, len(s) + 1
        count, char_count = len(t), {}
        for c in t:
            char_count[c] = char_count.setdefault(c, 0) + 1
        while hi < end:
            if (char_count.setdefault(s[hi], 0) > 0):
                count -= 1
            char_count[s[hi]] = char_count.setdefault(s[hi], 0) - 1
            hi += 1
            while count == 0:
                if hi - lo < res_hi - res_lo:
                    res_lo, res_hi = lo, hi
                char_count[s[lo]] += 1
                if char_count[s[lo]] > 0:
                    count += 1
                lo += 1
        print(res_lo, res_hi, count)
        if res_hi <= len(s):
            return s[res_lo: res_hi]
        else:
            return ""
