#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (35.04%)
# Total Accepted:    246.3K
# Total Submissions: 702.9K
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, determine if it has a cycle in it.
# 
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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        walker = runner = head
        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False
    
