#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (36.52%)
# Total Accepted:    163.1K
# Total Submissions: 446.6K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example,
# Given
# 
# 
# ⁠        1
# ⁠       / \
# ⁠      2   5
# ⁠     / \   \
# ⁠    3   4   6
# 
# 
# 
# 
# The flattened tree should look like:
# 
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠     \
# ⁠      3
# ⁠       \
# ⁠        4
# ⁠         \
# ⁠          5
# ⁠           \
# ⁠            6
# 
# 
# click to show hints.
# 
# Hints:
# 
# If you notice carefully in the flattened tree, each node's right child points
# to the next node of a pre-order traversal.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        parent = root
        while stack:
            # print([i.val for i in stack])
            node = stack.pop()
            if parent != node:
                parent.left = None
                parent.right = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            parent = node
        return
