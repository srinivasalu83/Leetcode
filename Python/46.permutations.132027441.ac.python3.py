#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (47.28%)
# Total Accepted:    230.7K
# Total Submissions: 488K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a collection of distinct numbers, return all possible permutations.
# 
# 
# 
# For example,
# [1,2,3] have the following permutations:
# 
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.current = []
        self.ret = []
        self._permute(nums[:])
        return self.ret
    
    def _permute(self, nums):
        # print(nums)
        if not nums:
            self.ret.append(self.current[:])
        else:
            for i, v in enumerate(nums):
                self.current.append(v)
                temp = nums[:]
                del temp[i]
                self._permute(temp)
                self.current.pop()
            
