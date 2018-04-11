#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (27.51%)
# Total Accepted:    153.5K
# Total Submissions: 557.9K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.
# 
# Note: The solution set must not contain duplicate quadruplets.
# 
# 
# 
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for ii in range(len(nums) - 3):
            if (ii > 0 and nums[ii] == nums[ii-1]):
                continue
            for jj in range(ii+1, len(nums)-2):
                if (jj > ii + 1 and nums[jj] == nums[jj-1]):
                    continue
                twosum = nums[ii] + nums[jj]
                head = jj + 1
                tail = len(nums) - 1
                while (head < tail):
                    foursum = twosum + nums[head] + nums[tail]
                    if (foursum == target):
                        res.append([nums[ii], nums[jj], nums[head], nums[tail]])
                        #print([ii, jj, head, tail])
                        while (head < tail and nums[head] == nums[head+1]):
                            head = head + 1
                        while (head < tail and nums[tail] == nums[tail-1]):
                            tail = tail - 1
                        head = head + 1
                        tail = tail - 1
                    elif (foursum < target):
                        head = head + 1
                    else:
                        tail = tail - 1
        return res
    
