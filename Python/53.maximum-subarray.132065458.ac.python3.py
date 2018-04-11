#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (40.30%)
# Total Accepted:    301.7K
# Total Submissions: 748.8K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
# 
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # opt_not_take[i]: the largest sum we can get with the first i elements without taking the last element
        # opt_take[i]: ... taking the last element
        for v in nums:
            if v >= 0:
                break
        else:
            return max(nums)
        opt_not_take, opt_take = [0], [0]
        for i, v in enumerate(nums):
            tmp = max(opt_take[i], opt_not_take[i])
            opt_take.append(max(opt_take[i] + v, v))
            opt_not_take.append(max(opt_take[i], opt_not_take[i]))
        # print(opt_not_take, opt_take)
        return max(opt_take[-1], opt_not_take[-1])
