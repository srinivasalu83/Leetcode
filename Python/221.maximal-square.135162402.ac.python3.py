#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (30.32%)
# Total Accepted:    86K
# Total Submissions: 283.6K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# 
# For example, given the following matrix:
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Return 4.
# 
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        for i, row in enumerate(matrix):
            row = matrix[i] = list(map(int, row))
            for j, col in enumerate(row):
                if i * j * col:
                    row[j] = min(matrix[i-1][j], row[j-1], matrix[i-1][j-1]) + 1
        return max(map(max, matrix + [[0]])) ** 2
