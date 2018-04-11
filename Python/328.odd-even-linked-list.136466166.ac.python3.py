#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (44.75%)
# Total Accepted:    91.6K
# Total Submissions: 204.7K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
# 
# 
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.
# 
# 
# Note:
# The relative order inside both the even and odd groups should remain as it
# was in the input. 
# The first node is considered odd, the second node even and so on ...
# 
# 
# Credits:Special thanks to @DjangoUnchained for adding this problem and
# creating all test cases.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd_head, even_head = ListNode(0), ListNode(0)
        po, pe = odd_head, even_head
        is_odd = True
        while head:
            if is_odd:
                po.next = head
                po = head
            else:
                pe.next = head
                pe = head
            head = head.next
            is_odd = not is_odd
        pe.next = None
        po.next = even_head.next
        return odd_head.next
                
