#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Easy (51.81%)
# Total Accepted:    25.3K
# Total Submissions: 48.9K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array.
# (If there is no island, the maximum area is 0.)
# 
# Example 1:
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Given the above grid, return 6.
# 
# Note the answer is not 11, because the island must be connected
# 4-directionally.
# 
# 
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# 
# 
# Note:
# The length of each dimension in the given grid does not exceed 50.
# 
#
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        else:
            res = 0
            m, n = len(grid), len(grid[0])
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        res = max(res, self.sink(grid, i, j, m, n))
            return res
        
    def sink(self, grid, i, j, m, n):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
            grid[i][j] = 0
            res = sum([1, self.sink(grid, i, j - 1, m, n), self.sink(grid, i, j + 1, m, n), \
                      self.sink(grid, i - 1, j, m, n), self.sink(grid, i + 1, j, m, n)])
            return res
        else:
            return 0
