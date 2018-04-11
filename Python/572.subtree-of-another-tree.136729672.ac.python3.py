#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (40.20%)
# Total Accepted:    44.8K
# Total Submissions: 111.4K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# 
# Example 1:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# Example 2:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# Return false.
# 
#
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s_preorder = self.preorder(s)
        t_preorder = self.preorder(t)
        print(t_preorder , s_preorder)
        return t_preorder in s_preorder
    
    def preorder(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                res.append('*')
        return '#' + '#'.join(res) + '#'
