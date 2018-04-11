#
# [654] Maximum Binary Tree
#
# https://leetcode.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (69.77%)
# Total Accepted:    30.1K
# Total Submissions: 43.1K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 
# Given an integer array with no duplicates. A maximum tree building on this
# array is defined as follow:
# 
# The root is the maximum number in the array. 
# The left subtree is the maximum tree constructed from left part subarray
# divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray
# divided by the maximum number. 
# 
# 
# 
# 
# Construct the maximum tree by the given array and output the root node of
# this tree.
# 
# 
# Example 1:
# 
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    / 
# ⁠    2  0   
# ⁠      \
# ⁠       1
# 
# 
# 
# Note:
# 
# The size of the given array will be in the range [1,1000].
# 
# 
#
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self._construct(nums, 0, len(nums) - 1)
        
    def _construct(self, nums, i, j):
        if i > j:
            return None
        else:
            maxx_ind, maxx = max(enumerate(nums[i: j + 1]), key=lambda x: x[1])
            maxx_ind += i
            root = TreeNode(maxx)
            root.left = self._construct(nums, i, maxx_ind - 1)
            root.right = self._construct(nums, maxx_ind + 1, j)
            return root
