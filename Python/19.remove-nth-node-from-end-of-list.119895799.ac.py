#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (33.99%)
# Total Accepted:    242.1K
# Total Submissions: 712.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the nth node from the end of list and return its
# head.
# 
# For example,
# 
# 
# ⁠  Given linked list: 1->2->3->4->5, and n = 2.
# 
# ⁠  After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# Given n will always be valid.
# Try to do this in one pass.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        que = collections.deque(maxlen=n+1)
        pointer = head
        length = 0
        while (pointer != None):
            que.appendleft(pointer)
            pointer = pointer.next
            length = length + 1
        if (length == n):
            return head.next
        pointer = que.pop()
        pointer.next = pointer.next.next
        return head
