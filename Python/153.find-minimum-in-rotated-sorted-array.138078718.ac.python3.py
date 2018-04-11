#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (40.86%)
# Total Accepted:    191.7K
# Total Submissions: 469.3K
# Testcase Example:  '[1]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
#
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[start]
