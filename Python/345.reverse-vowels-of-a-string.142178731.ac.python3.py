#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (39.21%)
# Total Accepted:    105.7K
# Total Submissions: 269.6K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# 
# Example 1:
# Given s = "hello", return "holle".
# 
# 
# 
# Example 2:
# Given s = "leetcode", return "leotcede".
# 
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
#
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        record = []
        for i, c in enumerate(s):
            if c in 'aeiouAEIOU':
                record.append(i)
        n = len(record)
        for i in range((n + 1) // 2):
            s[record[i]], s[record[n - i - 1]] = s[record[n - i - 1]], s[record[i]]
        return ''.join(s)
