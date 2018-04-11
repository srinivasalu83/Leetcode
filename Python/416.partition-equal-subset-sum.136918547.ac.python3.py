#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (38.84%)
# Total Accepted:    41.4K
# Total Submissions: 106.7K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# 
# Note:
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# Example 1:
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# Example 2:
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
#
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        summ = sum(nums)
        if summ // 2 != summ / 2:
            return False
        possibles = set([0])
        for v in nums:
            possibles = possibles.union([po + v for po in possibles])
        return summ // 2 in possibles
