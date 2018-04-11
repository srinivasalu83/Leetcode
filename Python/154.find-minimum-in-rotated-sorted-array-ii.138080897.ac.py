#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (37.84%)
# Total Accepted:    94.9K
# Total Submissions: 250.8K
# Testcase Example:  '[1]'
#
# 
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# 
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            print(start, end)
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] == nums[end]:
                if nums[start] < nums[mid]:
                    end = mid - 1
                elif nums[start] == nums[mid]:
                    while start < end and nums[start] == nums[mid]:
                        start += 1
                else:
                    end = mid
            else:
                if nums[start] <= nums[end]:
                    end = mid
                else:
                    end = mid
                    start += 1
        return nums[start]
