#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (50.28%)
# Total Accepted:    146.3K
# Total Submissions: 291K
# Testcase Example:  '[0,0]'
#
# 
# Given an array of n integers where n > 1, nums, return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Solve it without division and in O(n).
# 
# For example, given [1,2,3,4], return [24,12,8,6].
# 
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array
# does not count as extra space for the purpose of space complexity analysis.)
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums
        res = nums[:]
        for i in range(1, len(nums)):
            nums[i] = nums[i] * nums[i - 1]
        for i in reversed(range(0, len(nums) - 1)):
            res[i] = res[i] * res[i + 1]
        print(nums)
        print(res)
        res[0] = res[1]
        for i in range(1, len(nums) - 1):
            res[i] = nums[i - 1] * res[i + 1]
        res[-1] = nums[-2]
        return res
