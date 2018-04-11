#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (35.07%)
# Total Accepted:    160.5K
# Total Submissions: 457.5K
# Testcase Example:  '[1,1,2]'
#
# 
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# 
# 
# For example,
# [1,1,2] have the following unique permutations:
# 
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.current = []
        self.ret = []
        self._permute(nums[:])
        k = sorted(self.ret)
        return [k[i] for i in range(len(k)) if i == 0 or k[i] != k[i-1]]
        # return list(set(self.ret))
    
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
            
