#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (32.84%)
# Total Accepted:    141.2K
# Total Submissions: 429.9K
# Testcase Example:  '[]\n0'
#
# 
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
#
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        counter = Counter(nums[1: k + 1])
        for i, v in enumerate(nums):
            # print(i, v, counter)
            if counter.get(v, 0) > 0:
                return True
            counter[v] = counter.get(v, 0) + 1
            if i + 1 < len(nums):
                counter[nums[i + 1]] -= 1
            if i - k >= 0:
                counter[nums[i - k]] -= 1
            if i + k < len(nums) - 1:
                counter[nums[i + k + 1]] = counter.get(nums[i + k + 1], 0) + 1
        return False
