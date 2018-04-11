#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (42.81%)
# Total Accepted:    188K
# Total Submissions: 439.3K
# Testcase Example:  '3\n7'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# 
# Above is a 3 x 7 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
#
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mat = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
        return mat[m - 1][n - 1]
