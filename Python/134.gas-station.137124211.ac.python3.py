#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station/description/
#
# algorithms
# Medium (29.98%)
# Total Accepted:    102.1K
# Total Submissions: 340.5K
# Testcase Example:  '[4]\n[5]'
#
# 
# There are N gas stations along a circular route, where the amount of gas at
# station i is gas[i].
# 
# 
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from station i to its next station (i+1). You begin the journey with
# an empty tank at one of the gas stations.
# 
# 
# 
# Return the starting gas station's index if you can travel around the circuit
# once, otherwise return -1.
# 
# 
# 
# Note:
# The solution is guaranteed to be unique.
# 
#
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, end = len(gas) - 1, 0
        summ = gas[start] - cost[start]
        while start > end:
            if summ >= 0:
                summ += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                summ += gas[start] - cost[start]
        return start if summ >= 0 else -1
