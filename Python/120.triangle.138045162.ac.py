#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (34.88%)
# Total Accepted:    130.8K
# Total Submissions: 375K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for row in reversed(range(len(triangle) - 1)):
            upper_row = triangle[row]
            lower_row = triangle[row + 1]
            for col in range(len(upper_row)):
                upper_row[col] += min(lower_row[col], lower_row[col + 1])
        return triangle[0][0]
