#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (24.08%)
# Total Accepted:    234.6K
# Total Submissions: 974.3K
# Testcase Example:  '[2,1,3]'
#
# 
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# 
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Binary tree [2,1,3], return true.
# 
# 
# Example 2:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 
# Binary tree [1,2,3], return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack, node = [], root
        while node.left:
            node = node.left
        bar = node.val - 1
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if bar >= node.val:
                return False
            else:
                bar = node.val
            root = node.right
        return True
