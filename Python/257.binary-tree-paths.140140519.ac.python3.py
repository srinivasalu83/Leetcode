#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (41.24%)
# Total Accepted:    155.5K
# Total Submissions: 377K
# Testcase Example:  '[1,2,3,null,5]'
#
# 
# Given a binary tree, return all root-to-leaf paths.
# 
# 
# For example, given the following binary tree:
# 
# 
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 
# 
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        stack = [(root, [str(root.val)])]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                result.append('->'.join(path))
            else:
                if node.right:
                    stack.append((node.right, path + [str(node.right.val)]))
                if node.left:
                    stack.append((node.left, path + [str(node.left.val)]))
        return result
