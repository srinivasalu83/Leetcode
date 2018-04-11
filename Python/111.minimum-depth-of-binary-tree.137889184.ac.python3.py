#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (33.56%)
# Total Accepted:    210.9K
# Total Submissions: 628.5K
# Testcase Example:  '[]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 1
        level = [root]
        while True:
            new_level = []
            for node in level:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            level = new_level
            depth += 1
