#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (33.44%)
# Total Accepted:    154.8K
# Total Submissions: 463.1K
# Testcase Example:  '[]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        walker, runner = head, head.next
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
        crawler = head
        new_head = None
        while crawler != walker:
            crawler.next, crawler, new_head = new_head, crawler.next, crawler
        if runner:
            walker = walker.next
            crawler.next, crawler, new_head = new_head, crawler.next, crawler
        else:
            tmp = ListNode(walker.val)
            tmp.next = new_head
            new_head = tmp
        while walker:
            if walker.val != new_head.val:
                return False
            walker = walker.next
            new_head = new_head.next
        return True
            
