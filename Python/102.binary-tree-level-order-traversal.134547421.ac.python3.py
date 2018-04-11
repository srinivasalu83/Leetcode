#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (42.58%)
# Total Accepted:    233.8K
# Total Submissions: 549K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
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
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            level_res = []
            tmp_queue = []
            for node in queue:
                level_res.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            res.append(level_res)
            queue = tmp_queue
        return res
            
