#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (45.30%)
# Total Accepted:    138.5K
# Total Submissions: 305.8K
# Testcase Example:  '[1]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# 
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.calculate_total(root)
        return self._kthSmallest(root, k)
    
    def _kthSmallest(self, root, k):
        if not root:
            return None
        left_total = root.left.total if root.left else 0
        if left_total + 1 == k:
            return root.val
        elif left_total + 1 > k:
            return self._kthSmallest(root.left, k)
        else:
            return self._kthSmallest(root.right, k - left_total - 1)
        
    def calculate_total(self, root):
        if not root:
            return 0
        left_total = self.calculate_total(root.left) if root.left else 0
        right_total = self.calculate_total(root.right) if root.right else 0
        root.total = left_total + right_total + 1
        return left_total + right_total + 1
