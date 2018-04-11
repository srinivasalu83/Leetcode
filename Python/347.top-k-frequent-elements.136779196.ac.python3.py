#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (49.61%)
# Total Accepted:    101.2K
# Total Submissions: 204K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 
# Given a non-empty array of integers, return the k most frequent elements.
# 
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
# 
# 
# Note: 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
#
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stat = Counter(nums)
        return [v[0] for v in sorted(list(stat.items()), key=lambda x:x[1], reverse=True)[:k]]
