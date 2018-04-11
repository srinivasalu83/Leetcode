#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (41.12%)
# Total Accepted:    335.5K
# Total Submissions: 815.8K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        p1 = l1
        p2 = l2
        ll = None
        pp = None
        while (p1 != None and p2 != None):
            if (p1.val < p2.val):
                if (pp == None):
                    ll = p1
                else:
                    pp.next = p1
                pp = p1
                p1 = p1.next
            else:
                if (pp == None):
                    ll = p2
                else:
                    pp.next = p2
                pp = p2
                p2 = p2.next
        if (p1 != None):
            pp.next = p1
        elif (p2 != None):
            pp.next = p2
        return ll
