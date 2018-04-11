#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (23.47%)
# Total Accepted:    92.1K
# Total Submissions: 392.7K
# Testcase Example:  '[3, 30, 34, 5, 9]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
#
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        nums = list(map(str, nums))
        nums.sort(key = cmp_to_key(lambda x, y: 1 if x + y > y + x else (0 if x + y == y + x else -1)), reverse = True)
        return ''.join(nums).lstrip('0') or '0'
