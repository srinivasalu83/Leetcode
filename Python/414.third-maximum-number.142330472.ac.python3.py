#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (28.09%)
# Total Accepted:    58.4K
# Total Submissions: 208K
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
# 
# Example 1:
# 
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
# 
# 
# 
# Example 2:
# 
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
# 
# 
# 
# Example 3:
# 
# Input: [2, 2, 3, 1]
# 
# Output: 1
# 
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 
# 
#
from heapq import nlargest

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        return max(nums) if len(nums) <= 2 else nlargest(3, nums)[-1]
