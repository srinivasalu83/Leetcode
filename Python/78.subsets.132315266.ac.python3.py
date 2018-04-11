#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (44.75%)
# Total Accepted:    229.8K
# Total Submissions: 513.5K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# 
# For example,
# If nums = [1,2,3], a solution is:
# 
# 
# 
# [
# ⁠ [3],
# ⁠ [1],
# ⁠ [2],
# ⁠ [1,2,3],
# ⁠ [1,3],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.current, self.ret = [], []
        self._subsets(nums, 0, len(nums) - 1)
        return self.ret
    
    def _subsets(self, nums, lo, hi):
        # print(lo, hi)
        current, ret = self.current, self.ret
        ret.append(current[:])
        if lo > hi:
            return
        else:
            for i in range(lo, hi + 1):
                current.append(nums[i])
                self._subsets(nums, i + 1, hi)
                current.pop()
                
