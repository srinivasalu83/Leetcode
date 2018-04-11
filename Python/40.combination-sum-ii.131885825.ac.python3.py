#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (35.95%)
# Total Accepted:    149.3K
# Total Submissions: 415.2K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 
# Given a collection of candidate numbers (C) and a target number (T), find all
# unique combinations in C where the candidate numbers sums to T.
# 
# 
# Each number in C may only be used once in the combination.
# 
# Note:
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# 
# 
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# 
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
#
class Solution:
    def combinationSum2(self, candidates, target):
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
            if self.current not in self.ret:
                self.ret.append(self.current[:])
        elif pos < len(self.candidates) and target > 0:
            self.current.append(self.candidates[pos])
            self.search(target - self.candidates[pos], pos + 1)
            self.current.pop()
            self.search(target, pos + 1)
        return 

