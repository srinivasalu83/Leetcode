#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (39.10%)
# Total Accepted:    211K
# Total Submissions: 539.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Your algorithm should use only constant space. You may not modify the values
# in the list, only nodes itself can be changed.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head or not head.next):
            return head
        prev = ListNode(0)
        prev.next = head
        head = head.next
        while (prev.next and prev.next.next):
            pfor = prev.next
            plat = pfor.next
            temp = plat.next
            prev.next = plat
            plat.next = pfor
            pfor.next = temp
            prev = pfor
        return head
