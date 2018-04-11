#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (36.50%)
# Total Accepted:    136.6K
# Total Submissions: 374.2K
# Testcase Example:  '[[0]]'
#
# 
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in place.
# 
# 
# click to show follow up.
# 
# Follow up:
# 
# 
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = '#'
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = '#'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
        
