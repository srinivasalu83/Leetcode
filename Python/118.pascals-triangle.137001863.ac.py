#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (40.03%)
# Total Accepted:    168.4K
# Total Submissions: 420.6K
# Testcase Example:  '5'
#
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# For example, given numRows = 5,
# Return
# 
# 
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        while numRows > 1:
            former_row = res[-1]
            res.append([1] + [former_row[i] + former_row[i + 1] for i in range(len(former_row) - 1)] + [1])
            numRows -= 1
        return res
