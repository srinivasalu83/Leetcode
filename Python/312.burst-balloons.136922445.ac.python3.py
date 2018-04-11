#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (43.66%)
# Total Accepted:    37.8K
# Total Submissions: 86.6K
# Testcase Example:  '[3,1,5,8]'
#
# 
# ⁠   Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# ⁠   number on it represented by array nums.
# 
# ⁠   You are asked to burst all the balloons. If the you burst
# ⁠   balloon i you will get nums[left] * nums[i] * nums[right] coins. Here
# left
# ⁠   and right are adjacent indices of i. After the burst, the left and right
# ⁠   then becomes adjacent.
# 
# 
# ⁠   Find the maximum coins you can collect by bursting the balloons wisely.
# 
# 
# ⁠   Note: 
# ⁠   (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore
# you can not burst them.
# ⁠   (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 
# 
# 
# 
# ⁠   Example:
# 
# 
# ⁠   Given [3, 1, 5, 8]
# 
# 
# ⁠   Return 167
# 
# 
# ⁠   nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
# ⁠  coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
from collections import deque

class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for k in range(n - 2):
            for i in range(1, n - k - 1):
                j = i + k
                dp[i][j] = max(nums[i - 1] * nums[burst] * nums[j + 1] + dp[i][burst - 1] + dp[burst + 1][j] for burst in range(i, j + 1))
        return dp[1][n - 2]
