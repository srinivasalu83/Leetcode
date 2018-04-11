#
# [744] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Medium (34.80%)
# Total Accepted:    6.2K
# Total Submissions: 17.9K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# 
# There are N network nodes, labelled 1 to N.
# 
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
# 
# Now, we send a signal from a certain node K.  How long will it take for all
# nodes to receive the signal?  If it is impossible, return -1.
# 
# 
# Note:
# 
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1  and 1 .
# 
# 
#
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        def relax(adj_dict, u, v, distance, predecessor):
            inf = float('inf')
            d = distance[u] + adj_dict[u][v]
            if d < distance[v]:
                distance[v], predecessor[v] = d, u
    
        adj_dict = defaultdict(dict)
        for u, v, w in times:
            adj_dict[u - 1][v - 1] = w
        distance = [float('inf')] * N
        distance[K - 1] = 0
        predecessor, Q, visited = {}, [(0, K - 1)], set()
        while Q:
            _, u = heappop(Q)
            if u in visited:
                continue
            visited.add(u)
            for v in adj_dict[u].keys():
                relax(adj_dict, u, v, distance, predecessor)
                heappush(Q, (distance[v], v))
        delay_time = max(distance)
        return delay_time if delay_time != float('inf') else -1
