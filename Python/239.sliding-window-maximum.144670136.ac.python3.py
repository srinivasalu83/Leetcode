#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (34.17%)
# Total Accepted:    87.8K
# Total Submissions: 257.1K
# Testcase Example:  '[]\n0'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# 
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
# 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Therefore, return the max sliding window as [3,3,5,5,6,7].
# 
# Note: 
# You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for
# non-empty array.
# 
# Follow up:
# Could you solve it in linear time?
#
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        res = []
        dq = deque()  # store index
        for i in range(len(nums)):
            if dq and dq[0]<i-k+1:  # out of the window
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:  # remove impossible candidate
                dq.pop()
            dq.append(i)
            if i > k-2:
                res.append(nums[dq[0]])
        return res
