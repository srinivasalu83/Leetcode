#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (28.63%)
# Total Accepted:    477.5K
# Total Submissions: 1.7M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l1
        pl1, pl2 = None, None
        while l1 and l2:
            l1.val += l2.val
            pl1, l1 = l1, l1.next
            pl2, l2 = l2, l2.next
        if not l1:
            pl1.next = l2
        pp, p = None, head
        ten = 0
        while p:
            p.val += ten
            ten, p.val = p.val // 10, p.val % 10
            pp, p = p, p.next
        if ten != 0:
            pp.next = ListNode(ten)
        return head
