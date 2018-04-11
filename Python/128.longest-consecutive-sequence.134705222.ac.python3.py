#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (38.25%)
# Total Accepted:    138.1K
# Total Submissions: 361K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# 
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:
# 4.
# 
# 
# Your algorithm should run in O(n) complexity.
# 
#
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_len = 0
        while nums:
            n = nums.pop()
            len1 = len2 = 0
            i = n - 1
            while i in nums:
                nums.remove(i)
                i -= 1
                len1 += 1
            i = n + 1
            while i in nums:
                nums.remove(i)
                i += 1
                len2 += 1
            max_len = max(max_len, len1 + len2 + 1)
        return max_len
