#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (48.67%)
# Total Accepted:    39.7K
# Total Submissions: 81.5K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
# 
# 
# Example:
# 
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
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
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # reversed inorder traversal
        if not root:
            return root
        res = root
        stack = []
        current_sum = 0
        while True:
            while root:
                stack.append(root)
                root = root.right
            if not stack:
                return res
            node = stack.pop()
            node.val = current_sum = node.val + current_sum
            root = node.left
        return res
            
