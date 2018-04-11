#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
#
# algorithms
# Medium (36.81%)
# Total Accepted:    147.1K
# Total Submissions: 399.7K
# Testcase Example:  '[1,1,1,2,2,3]'
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
# 
# Your function should return length = 5, with the first five elements of nums
# being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new
# length.
# 
#
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ptr = 0
        last = '#'
        current = 0
        for i, v in enumerate(nums):
            current = 1 if v != last else current + 1
            last = v
            if current <= 2:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                ptr += 1
        print(nums, ptr)
        return ptr
