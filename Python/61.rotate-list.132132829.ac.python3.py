#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (24.45%)
# Total Accepted:    135.6K
# Total Submissions: 554.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a list, rotate the list to the right by k places, where k is
# non-negative.
# 
# 
# 
# Example:
# 
# Given 1->2->3->4->5->NULL and k = 2,
# 
# return 4->5->1->2->3->NULL.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        p, t = head, 0
        while p:
            p = p.next
            t += 1
        k = t - (k % t)
        p = head
        for i in range(k - 1):
            p = p.next
            if not p:
                return head
        if not p.next:
            return head
        q = p.next
        while q.next:
            q = q.next
        q.next = head
        head = p.next
        p.next = None
        return head
