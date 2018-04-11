#
# [808] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (34.98%)
# Total Accepted:    4.5K
# Total Submissions: 12.9K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
# 
# 
# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
# 
# 
# Note:
# 
# 
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
# 
#
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            ind = -1
            for c in word:
                ind = S.find(c, ind + 1)
                if ind == -1:
                    break
            else:
                count += 1
        return count
