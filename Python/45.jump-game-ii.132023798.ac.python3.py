#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (26.09%)
# Total Accepted:    113.9K
# Total Submissions: 436.6K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# For example:
# Given array A = [2,3,1,1,4]
# 
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from
# index 0 to 1, then 3 steps to the last index.)
# 
# Note:
# You can assume that you can always reach the last index.
# 
#
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        opt = [length] * length
        opt[0] = 0
        i = 0
        while i < length:
            lo, hi = i + 1, min(length - 1, i + nums[i]) # inclusive hi
            for j in range(lo, hi + 1):
                opt[j] = min(opt[j], opt[i] + 1)
            i, j = lo, lo
            while j <= hi:
                if nums[j] + j >= nums[i] + i:
                    i = j
                j += 1
        return opt[-1]
        
