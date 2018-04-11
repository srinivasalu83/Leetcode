#
# [697] Degree of an Array
#
# https://leetcode.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (46.68%)
# Total Accepted:    19.1K
# Total Submissions: 40.9K
# Testcase Example:  '[1,2,2,3,1]'
#
# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.
# 
# Example 1:
# 
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,2,3,1,4,2]
# Output: 6
# 
# 
# 
# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
# 
#
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        max_freq = 0
        for i, v in enumerate(nums):
            freq.setdefault(v, []).append(i)
            max_freq = max(max_freq, len(freq[v]))
        res = len(nums)
        for v, l in freq.items():
            if len(l) == max_freq:
                res = min(res, l[-1] - l[0] + 1)
        return res
