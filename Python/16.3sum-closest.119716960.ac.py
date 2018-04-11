#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (31.65%)
# Total Accepted:    171.8K
# Total Submissions: 542.9K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array S of n integers, find three integers in S such that the sum is
# closest to a given number, target. Return the sum of the three integers. You
# may assume that each input would have exactly one solution.
# 
# 
# ⁠   For example, given array S = {-1 2 1 -4}, and target = 1.
# 
# ⁠   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        closest = sum(nums[0:3])
        for ii in range(len(nums) - 2):
            head = ii + 1
            tail = len(nums) - 1
            while (head < tail):
                current = nums[ii] + nums[head] + nums[tail]
                if (abs(current - target) < abs(closest - target)):
                    closest = current
                if (current < target):
                    head = head + 1
                elif (current > target):
                    tail = tail - 1
                else:
                    return target
        return closest
