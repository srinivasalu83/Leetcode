#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (38.90%)
# Total Accepted:    122.2K
# Total Submissions: 314K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# 
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is
# 4. Note that there may be more than one LIS combination, it is only necessary
# for you to return the length.
# 
# 
# Your algorithm should run in O(n2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity? 
# 
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
            # print(tails)
        return size
