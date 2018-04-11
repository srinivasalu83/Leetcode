#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (34.93%)
# Total Accepted:    212.6K
# Total Submissions: 608.7K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        else:
            return sum in self.sums(root)
        
    def sums(self, root):
        if not root.left and not root.right:
            return {root.val}
        elif root.left and root.right:
            return {v + root.val for v in self.sums(root.left) | self.sums(root.right)}
        elif root.left:
            return {v + root.val for v in self.sums(root.left)}
        else:
            return {v + root.val for v in self.sums(root.right)}
