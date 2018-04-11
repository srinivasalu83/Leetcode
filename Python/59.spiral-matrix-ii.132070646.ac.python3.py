#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (40.99%)
# Total Accepted:    99.8K
# Total Submissions: 243.5K
# Testcase Example:  '3'
#
# Given an integer n, generate a square matrix filled with elements from 1 to
# n2 in spiral order.
# 
# For example,
# Given n = 3,
# 
# You should return the following matrix:
# 
# 
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
# 
#
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = [[0 for i in range(n)] for j in range(n)]
        left_corner, right_corner = [0, 0], [n - 1, n - 1]
        count, total, direction = 0, n * n, 'r'
        i, j = 0, 0
        while count < total:
            if direction == 'r':
                for j in range(left_corner[1], right_corner[1] + 1):
                    count += 1
                    matrix[i][j] = count
                left_corner[0] += 1
                direction = 'd'
            elif direction == 'd':
                for i in range(left_corner[0], right_corner[0] + 1):
                    count += 1
                    matrix[i][j] = count
                right_corner[1] -= 1
                direction = 'l'
            elif direction == 'l':
                for j in range(right_corner[1], left_corner[1] - 1, -1):
                    count += 1
                    matrix[i][j] = count
                right_corner[0] -= 1
                direction = 'u'
            else: # direction == 'u'
                for i in range(right_corner[0], left_corner[0] - 1, -1):
                    count += 1
                    matrix[i][j] = count
                left_corner[1] += 1
                direction = 'r'
            # print(left_corner, right_corner, matrix)
        return matrix
