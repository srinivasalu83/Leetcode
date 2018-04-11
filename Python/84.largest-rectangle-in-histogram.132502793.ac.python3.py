#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (27.59%)
# Total Accepted:    115.7K
# Total Submissions: 419.5K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
# 
#
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [0]
        r = 0
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] -1
                r = max(r, w*h)
            stack.append(i)
        return r
