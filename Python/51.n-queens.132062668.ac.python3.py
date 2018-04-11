#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (33.30%)
# Total Accepted:    98.3K
# Total Submissions: 295.2K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
# 
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
# 
# [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 
#
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.indicator = [[True for i in range(n)] for j in range(n)]
        self.current = []
        self.ret = []
        self.update = {}
        self._search(0, n - 1)
        return self.ret

    def _search(self, i, end):
        indicator, current, ret, update = self.indicator, self.current, self.ret, self.update
        # print(i, end, indicator, current, update)
        current_row = indicator[i]
        if i == end:
            for j, bo in enumerate(current_row):
                if bo:
                    # print('found')
                    current.append('.' * j + 'Q' + '.' * (end - j))
                    ret.append(current[:])
                    current.pop()
        else:
            for j, bo in enumerate(current_row):
                if bo:
                    current.append('.' * j + 'Q' + '.' * (end - j))
                    for k in range(i + 1, end + 1):
                        update.setdefault(i, [])
                        if indicator[k][j]:
                            update[i].append((k, j))
                            indicator[k][j] = False
                        if j - k + i >= 0 and indicator[k][j - k + i]:
                            update[i].append((k, j - k + i))
                            indicator[k][j - k + i] = False
                        if j + k - i <= end and indicator[k][j + k - i]:
                            update[i].append((k, j + k - i))
                            indicator[k][j + k - i] = False
                    self._search(i + 1, end)
                    current.pop()
                    self._undo(i)

    def _undo(self, lnum):
        l = self.update[lnum]
        indicator = self.indicator
        for i, j in l:
            indicator[i][j] = True
        self.update[lnum] = []
        
