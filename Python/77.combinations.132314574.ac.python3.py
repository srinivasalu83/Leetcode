#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (41.29%)
# Total Accepted:    141.9K
# Total Submissions: 343.6K
# Testcase Example:  '4\n2'
#
# 
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# 
# For example,
# If n = 4 and k = 2, a solution is:
# 
# 
# 
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.current, self.ret = [], []
        self._combine(1, n, k)
        return self.ret
    
    def _combine(self, lo, hi, k):
        # print(lo, hi, k)
        current, ret = self.current, self.ret
        if k == 0:
            ret.append(current[:])
            # print('found:', current)
        elif lo > hi:
            return
        else:
            for i in range(lo, hi + 1):
                current.append(i)
                self._combine(i + 1, hi, k - 1)
                current.pop()
                
