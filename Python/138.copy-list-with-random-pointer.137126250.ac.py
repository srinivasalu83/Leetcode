#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (25.84%)
# Total Accepted:    152.2K
# Total Submissions: 589.1K
# Testcase Example:  '{}'
#
# 
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# 
# 
# Return a deep copy of the list.
# 
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node = head
        while node:
            copy = RandomListNode(node.label)
            copy.next = node.next
            node.next = copy
            node = copy.next

        # Set each copy's .random
        node = head
        while node:
            node.next.random = node.random and node.random.next
            node = node.next.next

        # Separate the copied list from the original, (re)setting every .next
        node = head
        copy = head_copy = head and head.next
        while node:
            node.next = node = copy.next
            copy.next = copy = node and node.next

        return head_copy
