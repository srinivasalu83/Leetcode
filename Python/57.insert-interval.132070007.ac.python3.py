#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (28.99%)
# Total Accepted:    124.4K
# Total Submissions: 429.1K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# 
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
# 
# 
# 
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as
# [1,2],[3,10],[12,16].
# 
# 
# 
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
# 
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        i = 0
        intervals.sort(key=lambda x: x.start)
        while i < len(intervals) - 1:
            if intervals[i].end < intervals[i + 1].start:
                i += 1
            else:
                intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
                del intervals[i + 1]
        return intervals
