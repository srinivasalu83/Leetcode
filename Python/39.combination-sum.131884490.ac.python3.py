#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (41.40%)
# Total Accepted:    214.5K
# Total Submissions: 518K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 
# Given a set of candidate numbers (C) (without duplicates) and a target number
# (T), find all unique combinations in C where the candidate numbers sums to
# T. 
# 
# 
# The same repeated number may be chosen from C unlimited number of times.
# 
# 
# Note:
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# 
# 
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# 
# [
# ⁠ [7],
# ⁠ [2, 2, 3]
# ]
# 
# 
#
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ret = []
        candidates.sort()
        candidates.reverse()
        self.candidates = candidates
        self.current = []
        self.search(target, 0)
        return self.ret
    
    def search(self, target, pos):
        if target == 0:
            self.ret.append(self.current[:])
        elif pos < len(self.candidates) and target > 0:
            self.current.append(self.candidates[pos])
            self.search(target - self.candidates[pos], pos)
            self.current.pop()
            self.search(target, pos + 1)
        return 

