#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (46.64%)
# Total Accepted:    35.3K
# Total Submissions: 75.6K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# 
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
# 
#
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            dis = {}
            for q in points:
                d = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                dis[d] = dis.get(d, 0) + 1
            for k in dis:
                res += dis[k] * (dis[k] - 1)
        return res
