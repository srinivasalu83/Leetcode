#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (34.16%)
# Total Accepted:    137.3K
# Total Submissions: 401.9K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # print(preorder, inorder)
        if not inorder:
            return None
        root_val = preorder.pop(0)
        inorder_root_val_ind = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder, inorder[0: inorder_root_val_ind])
        root.right = self.buildTree(preorder, inorder[inorder_root_val_ind + 1:])
        return root
