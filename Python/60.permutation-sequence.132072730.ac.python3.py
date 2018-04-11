#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (29.49%)
# Total Accepted:    101.2K
# Total Submissions: 343.1K
# Testcase Example:  '3\n1'
#
# The set [1,2,3,…,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 
# 
# Given n and k, return the kth permutation sequence.
# 
# Note: Given n will be between 1 and 9 inclusive.
# 
#
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial
        candidates = [i for i in range(1, n + 1)]
        ret = []
        for i in reversed(range(n)):
            f = factorial(i)
            tmp = (k - 1) // f
            ret.append(str(candidates[tmp]))
            del candidates[tmp]
            k = k % f
            # print(ret, candidates)
        return ''.join(ret)
