#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (19.65%)
# Total Accepted:    100.8K
# Total Submissions: 512.7K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# 
# 
# For example,
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 
# 
# After running your function, the board should be:
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
#
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for j in range(n):
            self.mark_boarder(board, 0, j, m, n)
            self.mark_boarder(board, m - 1, j, m, n)
        for i in range(m):
            self.mark_boarder(board, i, 0, m, n)
            self.mark_boarder(board, i, n - 1, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'
    
    def mark_boarder(self, board, i, j, m, n):
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'B'
            self.mark_boarder(board, i - 1, j, m, n)
            self.mark_boarder(board, i + 1, j, m, n)
            self.mark_boarder(board, i, j - 1, m, n)
            self.mark_boarder(board, i, j + 1, m, n)
            
        
