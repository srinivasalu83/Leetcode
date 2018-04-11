#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (29.50%)
# Total Accepted:    162.3K
# Total Submissions: 550.3K
# Testcase Example:  '[2,3,1,1,4]'
#
# 
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# 
# Each element in the array represents your maximum jump length at that
# position. 
# 
# 
# Determine if you are able to reach the last index.
# 
# 
# 
# For example:
# A = [2,3,1,1,4], return true.
# 
# 
# A = [3,2,1,0,4], return false.
# 
#
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        des = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= des:
                des = i
        return des == 0
