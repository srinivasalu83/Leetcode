#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (38.29%)
# Total Accepted:    144K
# Total Submissions: 376.1K
# Testcase Example:  '[1,2,2]'
#
# 
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# 
# For example,
# If nums = [1,2,2], a solution is:
# 
# 
# 
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.current, self.ret = [], []
        self._subsetsWithDup(nums, 0, len(nums) - 1)
        return self.ret
    
    def _subsetsWithDup(self, nums, lo, hi):
        # print(lo, hi)
        current, ret = self.current, self.ret
        if current not in ret:
            ret.append(current[:])
        if lo > hi:
            return
        else:
            for i in range(lo, hi + 1):
                current.append(nums[i])
                self._subsetsWithDup(nums, i + 1, hi)
                current.pop()
                
