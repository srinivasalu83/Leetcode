#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (22.26%)
# Total Accepted:    95.9K
# Total Submissions: 430.9K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# 
# 
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
# 
# 
# 
# You should return the indices: [0,9].
# (order does not matter).
# 
#
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordsDict = {}
        wordsNum = len(words)
        for word in words:
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1
        wordLen = len(words[0])
        res = []
        for i in range(len(s) + 1 - wordLen * wordsNum):
            curr = {}
            j = 0
            while j < wordsNum:
                word = s[i + j * wordLen : i + j * wordLen + wordLen]
                if word not in wordsDict: 
                    break
                if word not in curr: 
                    curr[word] = 1
                else:
                    curr[word] += 1
                if curr[word] > wordsDict[word]:
                    break
                j += 1
            if j == wordsNum:
                res.append(i)
        return res
    
