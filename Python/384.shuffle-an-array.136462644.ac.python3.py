#
# [384] Shuffle an Array
#
# https://leetcode.com/problems/shuffle-an-array/description/
#
# algorithms
# Medium (47.29%)
# Total Accepted:    41.2K
# Total Submissions: 87.1K
# Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# Shuffle a set of numbers without duplicates.
# 
# 
# Example:
# 
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
# 
# // Shuffle the array [1,2,3] and return its result. Any permutation of
# [1,2,3] must equally likely to be returned.
# solution.shuffle();
# 
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
# 
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
# 
# 
#
from random import shuffle

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.shuffled_nums = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.shuffled_nums = self.nums[:]
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffle(self.shuffled_nums)
        return self.shuffled_nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
