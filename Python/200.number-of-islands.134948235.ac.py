#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (36.59%)
# Total Accepted:    170K
# Total Submissions: 464.6K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 11110110101100000000
# Answer: 1
# Example 2:
# 11000110000010000011
# Answer: 3
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        def sink(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i - 1, i + 1, i, i), (j, j, j + 1, j - 1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(m) for j in range(n))
    
    
    
