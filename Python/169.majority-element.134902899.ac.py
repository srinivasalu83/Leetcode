#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (48.00%)
# Total Accepted:    255.8K
# Total Submissions: 532.9K
# Testcase Example:  '[1]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_candidate = None
        count = 0
        for v in nums:
            if count == 0:
                majority_candidate = v
            if v != majority_candidate:
                count -= 1
            else:
                count += 1
            # print(v, count, majority_candidate)
        return majority_candidate
        #count = 0
        #for v in nums:
        #    if v is majority_candidate:
        #        count += 1
        #if count >= (len(nums) // 2):
        #    return majority_candidate
