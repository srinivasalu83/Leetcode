#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (38.92%)
# Total Accepted:    150K
# Total Submissions: 385.5K
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is greater than its neighbors.
# 
# Given an input array where num[i] ≠ num[i+1], find a peak element and return
# its index.
# 
# The array may contain multiple peaks, in that case return the index to any
# one of the peaks is fine.
# 
# You may imagine that num[-1] = num[n] = -∞.
# 
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function
# should return the index number 2.
# 
# click to show spoilers.
# 
# Note:
# Your solution should be in logarithmic complexity.
# 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        start, end = 0, len(nums) - 1
        while start < end:
            # print(start, end)
            mid = (start + end) // 2
            if nums[mid] >= max(nums[end], nums[start]):
                if (mid == 0 and nums[mid] > nums[mid + 1]) or \
                    (mid == len(nums) - 1 and nums[mid] > nums[mid - 1]) or \
                    nums[mid] > max(nums[mid - 1], nums[mid + 1]):
                        return mid
                if nums[mid + 1] > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[start] <= nums[mid] < nums[end]:
                start = mid + 1
            elif nums[start] > nums[mid] >= nums[end]:
                end = mid - 1
            else:
                start = mid + 1
        return start
