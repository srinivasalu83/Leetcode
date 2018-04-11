#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (39.96%)
# Total Accepted:    195.5K
# Total Submissions: 489.1K
# Testcase Example:  '[]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases. Also thanks to @ts for adding additional test cases.
#
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        opt = [0 for i in range(len(nums) + 1)]
        opt[1] = nums[0]
        for i in range(2, len(opt)):
            opt[i] = max(nums[i - 1] + opt[i - 2], opt[i - 1])
        return opt[-1]
