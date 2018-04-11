#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (36.77%)
# Total Accepted:    134.9K
# Total Submissions: 366.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        res = [[root.val]]
        left2right = False
        while level:
            new_level = []
            for node in reversed(level):
                if left2right:
                    if node.left:
                        new_level.append(node.left)
                    if node.right:
                        new_level.append(node.right)
                else:
                    if node.right:
                        new_level.append(node.right)
                    if node.left:
                        new_level.append(node.left)
            if not new_level:
                return res
            res.append([x.val for x in new_level])
            level = new_level
            left2right = not left2right
                
