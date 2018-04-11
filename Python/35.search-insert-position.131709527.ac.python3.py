#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.03%)
# Total Accepted:    249K
# Total Submissions: 622.1K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# 
# Example 3:
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# 
# Example 1:
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = int((lo + hi) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if nums[lo] >= target:
            return lo
        else:
            return lo + 1
