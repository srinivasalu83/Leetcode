#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (37.59%)
# Total Accepted:    151.9K
# Total Submissions: 404.2K
# Testcase Example:  '[[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]'
#
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# 
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
# 
# 
# 
# A partially filled sudoku which is valid.
# 
# 
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the
# filled cells need to be validated.
# 
#
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = [board[i][m] for m in range(9) if board[i][m] != '.']
            col = [board[m][i] for m in range(9) if board[m][i] != '.']
            if len(set(row)) != len(row):
                return False
            if len(set(col)) != len(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                rec = []
                for m in [i, i + 1, i + 2]:
                    for n in [j, j + 1, j + 2]:
                        if board[m][n] != '.':
                            rec.append(board[m][n])
                if len(set(rec)) != len(rec):
                    return False
        return True
