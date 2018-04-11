#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (31.36%)
# Total Accepted:    136.8K
# Total Submissions: 436.3K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# 
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# 
# return 1->4->3->2->5->NULL.
# 
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.
# 
#
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        new_head = ListNode(0)
        new_head.next = head
        count = 1
        part1_tail = new_head
        while count < m:
            part1_tail = part1_tail.next
            count += 1
        pre = part1_tail
        ptr = part1_tail.next
        while count <= n:
            if pre == part1_tail:
                pre, ptr = ptr, ptr.next
            else:
                pre.next = ptr.next
                ptr.next = part1_tail.next
                part1_tail.next = ptr
                ptr = pre.next
            count += 1
        return new_head.next
