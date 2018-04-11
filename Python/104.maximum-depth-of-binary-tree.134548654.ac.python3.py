#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (54.90%)
# Total Accepted:    324.8K
# Total Submissions: 591.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_depth = 1
        stack = [(root, 1)]
        while stack:
            node, current_depth = stack.pop()
            if node.left:
                stack.append((node.left, current_depth + 1))
                max_depth = max(max_depth, current_depth + 1)
            if node.right:
                stack.append((node.right, current_depth + 1))
                max_depth = max(max_depth, current_depth + 1)
        return max_depth
    
