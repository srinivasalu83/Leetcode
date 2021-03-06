#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (51.52%)
# Total Accepted:    280.6K
# Total Submissions: 544.5K
# Testcase Example:  '[0,1,0,3,12]'
#
# 
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# 
# 
# For example, given nums  = [0, 1, 0, 3, 12], after calling your function,
# nums should be [1, 3, 12, 0, 0].
# 
# 
# 
# Note:
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        available = 0
        for i, v in enumerate(nums):
            if v != 0:
                nums[i], nums[available] = nums[available], nums[i]
                available += 1
