#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (24.68%)
# Total Accepted:    469.7K
# Total Submissions: 1.9M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
#
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        i = 0
        longest = 0
        for j, c in enumerate(s):
            while c in seen:
                seen.discard(s[i])
                i += 1
            seen.add(c)
            longest = max(longest, j - i + 1)
        return longest
