#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (33.92%)
# Total Accepted:    127.8K
# Total Submissions: 376.7K
# Testcase Example:  '{}'
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? Would your previous solution
# still work?
# 
# Note:
# You may only use constant extra space.
# 
# 
# For example,
# Given the following binary tree,
# 
# ⁠        1
# ⁠      /  \
# ⁠     2    3
# ⁠    / \    \
# ⁠   4   5    7
# 
# 
# 
# After calling your function, the tree should look like:
# 
# ⁠        1 -> NULL
# ⁠      /  \
# ⁠     2 -> 3 -> NULL
# ⁠    / \    \
# ⁠   4-> 5 -> 7 -> NULL
# 
# 
#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        upper_current = root
        while upper_current:
            lower_head = None
            lower_ptr = None
            lower_pre = None
            while upper_current:
                if upper_current.left:
                    if lower_head == None:
                        lower_ptr = lower_pre = lower_head = upper_current.left
                    else:
                        lower_pre = lower_ptr
                        lower_ptr = upper_current.left
                        lower_pre.next = lower_ptr
                if upper_current.right:
                    if lower_head == None:
                        lower_ptr = lower_pre = lower_head = upper_current.right
                    else:
                        lower_pre = lower_ptr
                        lower_ptr = upper_current.right
                        lower_pre.next = lower_ptr
                upper_current = upper_current.next
            upper_current = lower_head
            
