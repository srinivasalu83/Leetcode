#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (29.93%)
# Total Accepted:    132.6K
# Total Submissions: 443K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode('#')
        new_head.next = head
        pre = p = new_head
        while p:
            if not p.next:
                if pre.next != p:
                    pre.next = p.next
                return new_head.next
            else:
                if p.val == p.next.val:
                    p = p.next
                else:
                    if pre.next != p:
                        pre.next = p.next
                        p = p.next
                    else:
                        pre = p
                        p = p.next
        return new_head.next
                        
