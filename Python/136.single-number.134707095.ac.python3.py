#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (55.41%)
# Total Accepted:    291.9K
# Total Submissions: 526.7K
# Testcase Example:  '[1]'
#
# Given an array of integers, every element appears twice except for one. Find
# that single one.
# 
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
#
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for v in nums:
            res = res ^ v
        return res
