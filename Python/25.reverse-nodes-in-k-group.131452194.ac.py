#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (31.70%)
# Total Accepted:    123.7K
# Total Submissions: 390.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# You may not alter the values in the nodes, only nodes itself may be changed.
# 
# Only constant memory is allowed.
# 
# For example,
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ii = 0
        tail = head
        stack = []
        while (ii < k):
            if tail == None:
                break
            ii = ii + 1
            stack.append(tail)
            tail = tail.next # tail not included
        if ii < k:
            return head
        head = stack.pop()
        ptr = head
        while len(stack) != 0:
            ptr.next = stack.pop()
            ptr = ptr.next
        ptr.next = self.reverseKGroup(tail, k)
        return head
