#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (46.86%)
# Total Accepted:    225.9K
# Total Submissions: 482.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# 
# For example:
# Given binary tree [1,null,2,3],
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 
# 
# return [1,2,3].
# 
# 
# Note: Recursive solution is trivial, could you do it iteratively?
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
