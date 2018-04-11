#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (25.24%)
# Total Accepted:    177.5K
# Total Submissions: 703.1K
# Testcase Example:  '[1]\n0'
#
# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
# [5,6,7,1,2,3,4]. 
# 
# Note:
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# 
# 
# [show hint]
# Hint:
# Could you do it in-place with O(1) extra space?
# 
# 
# Related problem: Reverse Words in a String II
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
