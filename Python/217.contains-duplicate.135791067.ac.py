#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (47.08%)
# Total Accepted:    211.2K
# Total Submissions: 448.5K
# Testcase Example:  '[]'
#
# 
# Given an array of integers, find if the array contains any duplicates. Your
# function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
# 
#
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        occur = set([])
        for v in nums:
            if v in occur:
                return True
            occur.add(v)
        return False
