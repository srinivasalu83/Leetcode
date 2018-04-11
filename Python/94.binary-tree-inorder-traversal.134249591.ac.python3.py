#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (49.72%)
# Total Accepted:    274.8K
# Total Submissions: 552.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
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
# return [1,3,2].
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res
