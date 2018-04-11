#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (46.74%)
# Total Accepted:    338.1K
# Total Submissions: 723.4K
# Testcase Example:  '[]'
#
# Reverse a singly linked list.
# 
# click to show more hints.
# 
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            head.next, head, new_head = new_head, head.next, head
        return new_head
