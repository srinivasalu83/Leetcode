#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (40.57%)
# Total Accepted:    204K
# Total Submissions: 502.7K
# Testcase Example:  '[1]\n1'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import heappush, heapreplace
        heap = []
        for v in nums:
            if len(heap) < k:
                heappush(heap, v)
            else:
                if v > heap[0]:
                    heapreplace(heap, v)
        return heap[0]
