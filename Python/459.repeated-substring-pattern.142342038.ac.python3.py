#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (38.22%)
# Total Accepted:    51.1K
# Total Submissions: 133.6K
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together.  You may
# assume the given string consists of lowercase English letters only and its
# length  will not exceed 10000. 
# 
# Example 1:
# 
# Input: "abab"
# 
# Output: True
# 
# Explanation: It's the substring "ab" twice.
# 
# 
# 
# Example 2:
# 
# Input: "aba"
# 
# Output: False
# 
# 
# 
# Example 3:
# 
# Input: "abcabcabcabc"
# 
# Output: True
# 
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)
# 
# 
#
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start_char = s[0]
        for i in range(1, len(s)):
            if s[i] == start_char:
                pattern = s[:i]
                for j in range(0, len(s), i):
                    if pattern != s[j: j + i]:
                        break
                else:
                    return True
        return False
        
