#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (33.42%)
# Total Accepted:    150.4K
# Total Submissions: 450K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
# 
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        pre, p = new_head, head
        while p:
            if p.val == val:
                pre.next = p.next
                p = pre.next
            else:
                pre, p = p, p.next
        return new_head.next
