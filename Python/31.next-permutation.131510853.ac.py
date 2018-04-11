#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (29.05%)
# Total Accepted:    148.1K
# Total Submissions: 509.8K
# Testcase Example:  '[1,2,3]'
#
# 
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ifMax = True
        for ii in reversed(range(len(nums) - 1)):
            if nums[ii + 1] > nums[ii]:
                ifMax = False
                break
        if ifMax:
            nums.sort()
            return
        kk = ii + 1
        for jj in range(ii + 2, len(nums)):
            if nums[jj] > nums[ii] and nums[jj] < nums[kk]:
                kk = jj
        temp = nums[kk]
        nums[kk] = nums[ii]
        nums[ii] = temp
        nums[ii+1:] = sorted(nums[ii+1:])
