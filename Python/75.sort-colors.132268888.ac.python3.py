#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (38.90%)
# Total Accepted:    217.5K
# Total Submissions: 559.1K
# Testcase Example:  '[0]'
#
# 
# Given an array with n objects colored red, white or blue, sort them so that
# objects of the same color are adjacent, with the colors in the order red,
# white and blue.
# 
# 
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# 
# 
# Note:
# You are not suppose to use the library's sort function for this problem.
# 
# 
# click to show follow up.
# 
# 
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with an one-pass algorithm using only constant space?
# 
# 
#
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0 # i for 0, j for 0 and 1
        for k, v in enumerate(nums):
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
                
