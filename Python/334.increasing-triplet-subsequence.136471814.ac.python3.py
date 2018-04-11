#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (39.76%)
# Total Accepted:    58.9K
# Total Submissions: 148.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given an unsorted array return whether an increasing subsequence of length 3
# exists or not in the array.
# 
# 
# Formally the function should:
# Return true if there exists i, j, k  
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 
# else return false.
# 
# 
# 
# Your algorithm should run in O(n) time complexity and O(1) space
# complexity.
# 
# 
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
# 
# 
# Given [5, 4, 3, 2, 1],
# return false.
# 
# 
# Credits:Special thanks to @DjangoUnchained for adding this problem and
# creating all test cases.
#
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
