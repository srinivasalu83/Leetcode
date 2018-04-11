#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (15.19%)
# Total Accepted:    92K
# Total Submissions: 605.9K
# Testcase Example:  '[]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
#
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import numpy as np

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        lines = {}
        for p in points:
            for q in points:
                if p != q:
                    if p.x == q.x:
                        line = (None, p.x)
                    else:
                        a = np.longdouble(p.y - q.y) / (p.x - q.x)
                        line = (a, p.y - a * p.x)
                    line_set = lines.setdefault(line, set([]))
                    line_set |= set([p, q])
        max_points = 0
        # print(lines)
        for i, s in lines.items():
            if len(s) > max_points:
                max_points = len(s)
        return max_points
