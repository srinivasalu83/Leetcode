#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (34.65%)
# Total Accepted:    155.7K
# Total Submissions: 449.5K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# 
# 
# For example,
# 
# Consider the following matrix:
# 
# 
# [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# 
# 
# Given target = 3, return true.
#
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            # print(lo, mid, hi)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            return False
        row = matrix[mid]
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            # print(lo, mid, hi)
            if row[mid] == target:
                return True
            elif target < row[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            return False
        
        
