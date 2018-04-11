#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (37.78%)
# Total Accepted:    134.4K
# Total Submissions: 355.6K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
# 
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# 
# For example,
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 
# 
# 
# 
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# 
# Return the sum = 12 + 13 = 25.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # root to leaf
        if not root:
            return 0
        self.res = 0
        self.accumulate(root, 0)
        return self.res

    def accumulate(self, root, acc):
        if not root.left and not root.right:
            self.res += acc * 10 + root.val
        else:
            if root.left:
                self.accumulate(root.left, acc * 10 + root.val)
            if root.right:
                self.accumulate(root.right, acc * 10 + root.val)
