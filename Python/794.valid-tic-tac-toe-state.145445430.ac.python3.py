#
# [810] Valid Tic-Tac-Toe State
#
# https://leetcode.com/problems/valid-tic-tac-toe-state/description/
#
# algorithms
# Medium (27.72%)
# Total Accepted:    3.1K
# Total Submissions: 11.3K
# Testcase Example:  '["O  ","   ","   "]'
#
# A Tic-Tac-Toe board is given as a string array board. Return True if and only
# if it is possible to reach this board position during the course of a valid
# tic-tac-toe game.
# 
# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".
# The " " character represents an empty square.
# 
# Here are the rules of Tic-Tac-Toe:
# 
# 
# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters, while the second player always
# places "O" characters.
# "X" and "O" characters are always placed into empty squares, never filled
# ones.
# The game ends when there are 3 of the same (non-empty) character filling any
# row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# 
# 
# 
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".
# 
# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.
# 
# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false
# 
# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
# 
# 
# Note:
# 
# 
# board is a length-3 array of strings, where each string board[i] has length
# 3.
# Each board[i][j] is a character in the set {" ", "X", "O"}.
# 
#
class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def examine(board):
            candidate = []
            for i in range(3):
                candidate.append(board[0][i] + board[1][i] + board[2][i]) # col
                candidate.append(board[i][0] + board[i][1] + board[i][2]) # row
            candidate.append(board[0][0] + board[1][1] + board[2][2])
            candidate.append(board[2][0] + board[1][1] + board[0][2])
            return candidate.count('XXX'), candidate.count('OOO')
        
        board_join = ''.join(board)
        total_X = board_join.count('X')
        total_O = board_join.count('O')
        candidate = []
        for i in range(3):
            candidate.append(board[0][i] + board[1][i] + board[2][i]) # col
            candidate.append(board[i][0] + board[i][1] + board[i][2]) # row
        candidate.append(board[0][0] + board[1][1] + board[2][2])
        candidate.append(board[2][0] + board[1][1] + board[0][2])
        win_X, win_O = candidate.count('XXX'), candidate.count('OOO')
        if total_X - total_O == 1:
            return win_O == 0 and win_X >= 0
        elif total_X - total_O == 0:
            return win_X == 0 and win_O >= 0
        else:
            return False
