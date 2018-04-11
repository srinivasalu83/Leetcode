#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (28.10%)
# Total Accepted:    173.6K
# Total Submissions: 617.8K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 
# Given a 2D board and a word, find if the word exists in the grid.
# 
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# 
# For example,
# Given board = 
# 
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
# 
#
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.path = []
        m, n = len(board), len(board[0])
        if not word or not board:
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    self.path.append((i, j))
                    if self.search(board, i, j, word, 1):
                        # print(self.path)
                        return True
                    self.path.pop()
        return False
    
    def search(self, board, i, j, word, k):
        if k == len(word):
            return True
        m, n, path = len(board), len(board[0]), self.path
        if i < m - 1 and board[i + 1][j] == word[k] and not (i + 1, j) in path:
            path.append((i + 1, j))
            if self.search(board, i + 1, j, word, k + 1):
                return True
            path.pop()         
        if j < n - 1 and board[i][j + 1] == word[k] and not (i, j + 1) in path:
            path.append((i, j + 1))
            if self.search(board, i, j + 1, word, k + 1):
                return True
            path.pop()
        if i > 0 and board[i - 1][j] == word[k] and not (i - 1, j) in path:
            path.append((i - 1, j))
            if self.search(board, i - 1, j, word, k + 1):
                return True
            path.pop()
        if j > 0 and board[i][j - 1] == word[k] and not (i, j - 1) in path:
            path.append((i, j - 1))
            if self.search(board, i, j - 1, word, k + 1):
                return True
            path.pop()
        return False
