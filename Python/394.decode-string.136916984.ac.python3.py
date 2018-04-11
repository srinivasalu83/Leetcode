#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (42.07%)
# Total Accepted:    51.6K
# Total Submissions: 122.6K
# Testcase Example:  '"3[a]2[bc]"'
#
# 
# Given an encoded string, return it's decoded string.
# 
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# 
# Examples:
# 
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# 
# 
#
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        p = 0
        while p < len(s):
            if s[p] == '[':
                stack.append(p)
                p += 1
            elif s[p] == ']':
                str_start = stack.pop() + 1
                str_end = p - 1
                digit_start = digit_end = str_start - 2
                while digit_start >= 0 and '0' <= s[digit_start] <= '9':
                    digit_start -= 1
                digit_start += 1
                time = int(s[digit_start : digit_end + 1])
                string = s[str_start : str_end + 1]
                s = s[:digit_start] + time * string + s[str_end + 2:]
                p = digit_start
            else:
                p += 1
            # print(s)
        return s
