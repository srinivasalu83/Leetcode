#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (26.81%)
# Total Accepted:    110.8K
# Total Submissions: 413.2K
# Testcase Example:  '[1,2,3,4]'
#
# 
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 
# You must do this in-place without altering the nodes' values.
# 
# 
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # count length
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        # reverse the second part
        mid = length // 2
        p, pre = head, None
        new_head = None
        while mid > 0:
            pre = p
            p = p.next
            mid -= 1
        pre.next = None
        while p:
            tmp_p = p
            p = p.next
            tmp_p.next = new_head
            new_head = tmp_p
        # combine
        p, q = head, new_head
        while p and q:
            next_p, next_q = p.next, q.next
            p.next, q.next = q, p.next if p.next else q.next
            p, q = next_p, next_q
        head = p
