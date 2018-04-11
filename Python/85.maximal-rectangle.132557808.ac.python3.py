#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (29.62%)
# Total Accepted:    84.8K
# Total Submissions: 286.5K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
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
# Return 6.
# 
#
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        maximum = 0
        m, n = len(matrix), len(matrix[0])
        height = [0 for j in range(n)]
        left = [0 for j in range(n)]
        right = [n for j in range(n)]
        for i in range(m):
            tmp_left, tmp_right = 0, n
            for j in range(n):
                height[j] = height[j] +  1 if matrix[i][j] == '1' else 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], tmp_left)
                else:
                    left[j] = 0
                    tmp_left = j + 1
            for j in reversed(range(n)):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], tmp_right)
                else:
                    right[j] = n
                    tmp_right = j
            for j in range(n):
                maximum = max(maximum, height[j] * (right[j] - left[j]))
            # print(height, left, right)
        return maximum
    
