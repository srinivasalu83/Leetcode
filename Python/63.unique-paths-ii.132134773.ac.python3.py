#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (32.16%)
# Total Accepted:    133.2K
# Total Submissions: 414.1K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# 
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# 
# [
# ⁠ [0,0,0],
# ⁠ [0,1,0],
# ⁠ [0,0,0]
# ]
# 
# 
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.
# 
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        mat = [[0 for j in range(n)] for i in range(m)]
        mat[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            if obstacleGrid[i - 1][0] == 1 or obstacleGrid[i][0] == 1:
                mat[i][0] = 0
            else:
                mat[i][0] = mat[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j - 1] == 1 or obstacleGrid[0][j] == 1:
                mat[0][j] = 0
            else:
                mat[0][j] = mat[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1 or obstacleGrid[i - 1][j] == obstacleGrid[i][j - 1] == 1:
                    mat[i][j] = 0
                elif obstacleGrid[i - 1][j] == 1:
                    mat[i][j] = mat[i][j - 1]
                elif obstacleGrid[i][j - 1] == 1:
                    mat[i][j] = mat[i - 1][j]
                else:
                    mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
        print(mat)
        return mat[m - 1][n - 1]
