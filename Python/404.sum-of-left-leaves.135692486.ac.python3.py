#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (47.52%)
# Total Accepted:    84.5K
# Total Submissions: 177.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                if not node.left.left and not node.left.right:
                    res += node.left.val
            if node.right:
                stack.append(node.right)
        return res
        
