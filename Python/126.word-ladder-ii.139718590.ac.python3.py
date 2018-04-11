#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (14.86%)
# Total Accepted:    81.8K
# Total Submissions: 550.2K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
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
# Return
# 
# ⁠ [
# ⁠   ["hit","hot","dot","dog","cog"],
# ⁠   ["hit","hot","lot","log","cog"]
# ⁠ ]
# 
# 
# 
# 
# Note:
# 
# Return an empty list if there is no such transformation sequence.
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
from collections import deque
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # search
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        wordSet.add(beginWord)
        front_pi = {beginWord: set()}
        end_pi = {endWord: set()}
        front_set = set([beginWord])
        end_set = set([endWord])
        front_seen = set([beginWord])
        end_seen = set([endWord])
        turn = False
        count = 1
        # bfs
        while front_set.isdisjoint(end_set):
            count += 1
            if not front_set:
                return []
            new_front_set = set()
            new_front_seen = copy.deepcopy(front_seen)
            for word in front_set:
                for c in string.ascii_lowercase:
                    for index in range(len(word)):
                        target = word[:index] + c + word[index+1:]
                        if target in wordSet and target not in front_seen:
                            new_front_set.add(target)
                            front_pi.setdefault(target, set()).add(word)
                            new_front_seen.add(target)
            front_set = new_front_set
            front_seen = new_front_seen # !!!!
            if len(front_set) > len(end_set):
                front_set, end_set = end_set, front_set
                front_pi, end_pi = end_pi, front_pi
                front_seen, end_seen = end_seen, front_seen
                turn = not turn
        # backtrace
        # combine them to get a directed graph
        if turn:
            front_pi, end_pi = end_pi, front_pi
        for child, parents in front_pi.items():
            for parent in parents:
                end_pi.setdefault(parent, set()).add(child)
        print(end_pi, count)
        # bfs
        result = []
        dq = deque([(beginWord, [beginWord])])
        while dq:
            word, path = dq.popleft()
            if word == endWord:
                result.append(path)
                continue
            for child in end_pi.get(word, []):
                dq.append((child, path + [child]))
        return result
