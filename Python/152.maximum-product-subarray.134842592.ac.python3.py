#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (26.74%)
# Total Accepted:    136.8K
# Total Submissions: 511.6K
# Testcase Example:  '[2,3,-2,4]'
#
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# 
#
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        opt_max = [0 for i in range(len(nums) + 1)] # max product containing the ith elem
        opt_min = [0 for i in range(len(nums) + 1)]
        for i, v in enumerate(nums):
            opt_max[i + 1] = max(v, v * opt_max[i], v * opt_min[i])
            opt_min[i + 1] = min(v, v * opt_max[i], v * opt_min[i])
        print(opt_max)
        print(opt_min)
        return max(opt_max)
