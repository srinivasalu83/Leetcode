#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (36.37%)
# Total Accepted:    343.8K
# Total Submissions: 945.3K
# Testcase Example:  '[1,1,2]'
#
# 
# Given a sorted array, remove the duplicates in-place such that each element
# appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# 
# Example:
# 
# Given nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.
# 
# 
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        ptr = 0
        for ii in range(1, len(nums)):
            if nums[ii] != nums[ptr]:
                ptr = ptr + 1
                nums[ptr] = nums[ii]
        return ptr + 1
