#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (27.15%)
# Total Accepted:    125K
# Total Submissions: 460.5K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a binary tree, find the maximum path sum.
# 
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# 
# For example:
# Given the below binary tree,
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 
# 
# Return 6.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_val = -2147283648
        self.at_least_one = False
        res = self._maxPathSum(root)
        if self.at_least_one:
            return max(res)
        else:
            return self.max_val
        
    def _maxPathSum(self, root):
        if not root:
            return 0, 0
        if root.val >= self.max_val:
            if root.val >= 0:
                self.at_least_one = True
            self.max_val = root.val
        if not root.left and not root.right:
            return root.val, 0 # inc, exc
        inc_left, exc_left = self._maxPathSum(root.left)
        inc_right, exc_right = self._maxPathSum(root.right)
        inc_root = max(root.val, root.val + inc_left, root.val + inc_right)
        exc_root = max(inc_left, exc_left, inc_right, exc_right, root.val + inc_left + inc_right)
        print(root.val, inc_root, exc_root)
        return inc_root, exc_root
    
