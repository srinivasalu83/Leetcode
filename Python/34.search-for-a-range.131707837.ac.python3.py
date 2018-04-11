#
# [34] Search for a Range
#
# https://leetcode.com/problems/search-for-a-range/description/
#
# algorithms
# Medium (31.59%)
# Total Accepted:    186.2K
# Total Submissions: 589.5K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers sorted in ascending order, find the starting and
# ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        return self._searchRange(nums, target, 0, len(nums) - 1)
        
    def _searchRange(self, nums, target, lo, hi):
        if lo == hi:
            if nums[lo] == target:
                return [lo, lo]
            else:
                return [-1, -1]
        mid = int((lo + hi) / 2)
        lo1, hi1 = self._searchRange(nums, target, lo, mid)
        lo2, hi2 = self._searchRange(nums, target, mid + 1, hi)
        if hi1 != -1 and lo2 != -1 and nums[hi1] == nums[lo2] == target: #nums[-1] is valid!!!
            return [lo1, hi2]
        elif lo1 != -1:
            return [lo1, hi1]
        elif lo2 != -1:
            return [lo2, hi2]
        else:
            return [-1, -1]
        
