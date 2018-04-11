#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (20.05%)
# Total Accepted:    161.1K
# Total Submissions: 803.7K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# 
# For example,
# 
# 
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# 
# 
# 
# Note:
# 
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# 
# 
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a
# set of strings). Please reload the code definition to get the latest changes.
# 
#
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordDict.discard(beginWord)
        while front:
            # generate all valid transformations
            front = wordDict & (set(word[:index] + ch + word[index+1:] for word in front 
                                for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
            if front & back:
                # there are common elements in front and back, done
                return length
            length += 1
            if len(front) > len(back):
                # swap front and back for better performance (fewer choices in generating nextSet)
                front, back = back, front
            # remove transformations from wordDict to avoid cycle
            wordDict -= front
            print(front, back)
        return 0

