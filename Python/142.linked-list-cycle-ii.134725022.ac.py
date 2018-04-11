#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (30.61%)
# Total Accepted:    144.7K
# Total Submissions: 472.6K
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# 
# 
# 
# Note: Do not modify the linked list.
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        walker = runner = head
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                new_walker = head
                while new_walker != walker:
                    new_walker = new_walker.next
                    walker = walker.next
                return walker
        return None
