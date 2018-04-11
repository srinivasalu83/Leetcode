#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (47.34%)
# Total Accepted:    35.2K
# Total Submissions: 74.5K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
# 
# 
# Example:
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
# 
# 
# 
# 
# Note:
# There are at least two nodes in this BST.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self._getMinimumDifference(root)[2]
    
    def _getMinimumDifference(self, root):
        # return min, max, min_diff
        if not root.left and not root.right:
            print(1, root.val, root.val, float('inf'))
            return root.val, root.val, float('inf')
        elif not root.left:
            minn2, maxx2, min_diff2 = self._getMinimumDifference(root.right)
            print(2, root.val, maxx2, min(min_diff2, minn2 - root.val))
            return root.val, maxx2, min(min_diff2, minn2 - root.val)
        elif not root.right:
            minn1, maxx1, min_diff1 = self._getMinimumDifference(root.left)
            print(2, minn1, root.val, min(min_diff1, root.val - maxx1))
            return minn1, root.val, min(min_diff1, root.val - maxx1)
        else:
            minn1, maxx1, min_diff1 = self._getMinimumDifference(root.left)
            minn2, maxx2, min_diff2 = self._getMinimumDifference(root.right)
            minn, maxx, min_diff = minn1, maxx2, min(min_diff1, min_diff2, root.val - maxx1, minn2 - root.val)
            print(4, minn, maxx, min_diff)
            return minn, maxx, min_diff
            
