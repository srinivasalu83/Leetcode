#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (32.24%)
# Total Accepted:    117.5K
# Total Submissions: 364.5K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: [2,3,1,2,4,3], s = 7
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # low inclusive, high exlcusive
        low, high = 0, 0
        current_sum = 0
        min_len = len(nums) + 10
        while high < len(nums):
            while high < len(nums) and current_sum < s:
                current_sum += nums[high]
                high += 1
            while low < high and current_sum >= s:
                current_sum -= nums[low]
                low += 1
            min_len = min(min_len, high - low + 1)
        return min_len if min_len <= len(nums) else 0
