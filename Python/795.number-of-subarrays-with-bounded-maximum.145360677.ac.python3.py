#
# [811] Number of Subarrays with Bounded Maximum
#
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
#
# algorithms
# Medium (40.41%)
# Total Accepted:    3.3K
# Total Submissions: 8.1K
# Testcase Example:  '[2,1,4,3]\n2\n3'
#
# We are given an array A of positive integers, and two positive integers L and
# R (L <= R).
# 
# Return the number of (contiguous, non-empty) subarrays such that the value of
# the maximum array element in that subarray is at least L and at most R.
# 
# 
# Example :
# Input: 
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2,
# 1], [3].
# 
# 
# Note:
# 
# 
# L, R  and A[i] will be an integer in the range [0, 10^9].
# The length of A will be in the range of [1, 50000].
# 
# 
#
class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        n = len(A)
        result = 0
        for i in range(n):
            maxx = 0
            for j in range(i, n):
                maxx = max(maxx, A[j])
                if R < maxx:
                    break
                elif L <= maxx:
                    result += 1
        return result
