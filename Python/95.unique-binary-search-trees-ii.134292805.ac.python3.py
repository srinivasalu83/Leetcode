#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (32.27%)
# Total Accepted:    100.5K
# Total Submissions: 311.3K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1...n.
# 
# 
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
# 
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        else:
            return self._generate(1, n)
        
    def _generate(self, start, end):
        print(start, end)
        res = []
        if start > end:
            return [None]
        for i in range(start, end + 1):
            lefts = self._generate(start, i - 1)
            rights = self._generate(i + 1, end)
            for l in lefts:
                for r in rights:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
    
