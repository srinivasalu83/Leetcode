#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (31.97%)
# Total Accepted:    193.6K
# Total Submissions: 605.5K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# 
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
# 
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        i = 0
        intervals.sort(key=lambda x: x.start)
        while i < len(intervals) - 1:
            if intervals[i].end < intervals[i + 1].start:
                i += 1
            else:
                intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
                del intervals[i + 1]
        return intervals
