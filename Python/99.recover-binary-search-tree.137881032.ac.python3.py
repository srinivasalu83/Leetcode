#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (31.07%)
# Total Accepted:    87.5K
# Total Submissions: 281.6K
# Testcase Example:  '[0,1]'
#
# 
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# 
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a
# constant space solution?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        inorder_nodes = []
        inorder_values = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            inorder_nodes.append(node)
            inorder_values.append(node.val)
            if node.right:
                root = node.right
        inorder_values.sort()
        for i, val in enumerate(inorder_values):
            inorder_nodes[i].val = val
