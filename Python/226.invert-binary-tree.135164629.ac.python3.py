#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (53.29%)
# Total Accepted:    227.8K
# Total Submissions: 427.5K
# Testcase Example:  '[]'
#
# Invert a binary tree.
# 
# 
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
# 
# to
# 
# 
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
# 
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# 
# Google: 90% of our engineers use the software you wrote (Homebrew), but you
# can’t invert a binary tree on a whiteboard so f*** off.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                node.left, node.right = node.right, node.left
        return root
