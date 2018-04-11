#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (27.28%)
# Total Accepted:    139.6K
# Total Submissions: 511.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# 
# 
# For example,
# Given the following matrix:
# 
# 
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# 
# You should return [1,2,3,6,9,8,7,4,5].
# 
#
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        left_corner, right_corner = [0, 0], [len(matrix) - 1, len(matrix[0]) - 1]
        total, direction, ret = (right_corner[0] + 1) * (right_corner[1] + 1), 'r', []
        i, j = 0, 0
        while len(ret) < total:
            if direction == 'r':
                for j in range(left_corner[1], right_corner[1] + 1):
                    ret.append(matrix[i][j])
                left_corner[0] += 1
                direction = 'd'
            elif direction == 'd':
                for i in range(left_corner[0], right_corner[0] + 1):
                    ret.append(matrix[i][j])
                right_corner[1] -= 1
                direction = 'l'
            elif direction == 'l':
                for j in range(right_corner[1], left_corner[1] - 1, -1):
                    ret.append(matrix[i][j])
                right_corner[0] -= 1
                direction = 'u'
            else: # direction == 'u'
                for i in range(right_corner[0], left_corner[0] - 1, -1):
                    ret.append(matrix[i][j])
                left_corner[1] += 1
                direction = 'r'
            # print(left_corner, right_corner, ret)
        return ret
