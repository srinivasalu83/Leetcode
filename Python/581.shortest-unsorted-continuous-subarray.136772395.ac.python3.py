#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (29.15%)
# Total Accepted:    32.7K
# Total Submissions: 112.2K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.  
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# 
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# 
# Note:
# 
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means . 
# 
# 
#
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        i = 0
        while i < len(nums) and nums[i] == sorted_nums[i]:
            i += 1
        j = len(nums) - 1
        while i <= j and nums[j] == sorted_nums[j]:
            j -= 1
        return j - i + 1
