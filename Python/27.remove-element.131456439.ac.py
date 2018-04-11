#
# [27] Remove Element
#
# https://leetcode.com/problems/remove-element/description/
#
# algorithms
# Easy (40.80%)
# Total Accepted:    272.5K
# Total Submissions: 667.9K
# Testcase Example:  '[3,2,2,3]\n3'
#
# Given an array and a value, remove all instances of that value in-place and
# return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.
# 
# Example:
# 
# 
# Given nums = [3,2,2,3], val = 3,
# 
# Your function should return length = 2, with the first two elements of nums
# being 2.
# 
# 
# 
# 
#
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return len(nums)
        ptr = 0
        for ii in range(len(nums)):
            if nums[ii] != val:
                nums[ptr] = nums[ii]
                ptr = ptr + 1
        return ptr
    
