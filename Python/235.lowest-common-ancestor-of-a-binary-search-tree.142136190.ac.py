#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (39.81%)
# Total Accepted:    191K
# Total Submissions: 479.9K
# Testcase Example:  '[2,1]\nnode with value 2\nnode with value 1'
#
# 
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
# 
# 
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# 
# ⁠       _______6______
# ⁠      /              \
# ⁠   ___2__          ___8__
# ⁠  /      \        /      \
# ⁠  0      _4       7       9
# ⁠        /  \
# ⁠        3   5
# 
# 
# 
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
# example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of
# itself according to the LCA definition.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.parent = None
        root.level = 0
        self._traverse(root)
        while p.level > q.level:
            p = p.parent
        while p.level < q.level:
            q = q.parent
        while p:
            if p == q:
                return p
            p = p.parent
            q = q.parent
        return None
    
    def _traverse(self, r):
        if r.left:
            r.left.parent = r
            r.left.level = r.level + 1
            self._traverse(r.left)
        if r.right:
            r.right.parent = r
            r.right.level = r.level + 1
            self._traverse(r.right)
