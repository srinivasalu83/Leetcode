#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (38.44%)
# Total Accepted:    222.2K
# Total Submissions: 578K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.cal_height(root)
        return self._isBalanced(root)
        
    def cal_height(self, root):
        if not root:
            return 0
        root.height = max(self.cal_height(root.left), self.cal_height(root.right)) + 1
        return root.height

    def _isBalanced(self, root):
        if not root:
            return True
        lh = 0 if not root.left else root.left.height
        rh = 0 if not root.right else root.right.height
        if abs(lh - rh) > 1:
            return False
        else:
            return self._isBalanced(root.left) and self._isBalanced(root.right)
        
