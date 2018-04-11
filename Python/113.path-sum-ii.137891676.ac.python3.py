#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (35.68%)
# Total Accepted:    161.7K
# Total Submissions: 453.2K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
# 
# 
# For example:
# Given the below binary tree and sum = 22,
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 
# return
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        current = []
        res = []
        self.dfs(root, sum, current, res)
        return res
    
    def dfs(self, root, summ, current, res):
        if not root.left and not root.right:
            if root.val == summ:
                res.append(current + [root.val])
        if root.left:
            current.append(root.val)
            self.dfs(root.left, summ - root.val, current, res)
            current.pop()
        if root.right:
            current.append(root.val)
            self.dfs(root.right, summ - root.val, current, res)
            current.pop()
