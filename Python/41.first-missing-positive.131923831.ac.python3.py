#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (25.83%)
# Total Accepted:    130.6K
# Total Submissions: 505.5K
# Testcase Example:  '[1,2,0]'
#
# 
# Given an unsorted integer array, find the first missing positive integer.
# 
# 
# 
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# 
# 
# 
# Your algorithm should run in O(n) time and uses constant space.
# 
#
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1] 
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp    
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] != i + 1:
                return i + 1
        return i + 2
