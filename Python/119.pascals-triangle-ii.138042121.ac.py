#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (38.20%)
# Total Accepted:    143.7K
# Total Submissions: 376.1K
# Testcase Example:  '3'
#
# Given an index k, return the kth row of the Pascal's triangle.
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
from collections import deque
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        q = deque([0, 1])
        while True:
            if q[0] == 0:
                if rowIndex == 0:
                    q.popleft()
                    return list(q)
                else:
                    rowIndex -= 1
                    q.append(0)
            q.append(q.popleft() + q[0])
