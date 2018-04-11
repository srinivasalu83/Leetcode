#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (40.13%)
# Total Accepted:    54.9K
# Total Submissions: 136.9K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.res = 0
        self._pathSum(root, sum)
        return self.res
        
    def _pathSum(self, root, sum):
        if not root:
            return []
        left = self._pathSum(root.left, sum) if root.left else []
        right = self._pathSum(root.right, sum) if root.right else []
        total = [v + root.val for v in left + right]
        total.append(root.val)
        self.res += total.count(sum) 
        return total
