#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (38.15%)
# Total Accepted:    105K
# Total Submissions: 275.2K
# Testcase Example:  '["MyQueue","empty"]\n[[],[]]'
#
# 
# Implement the following operations of a queue using stacks.
# 
# 
# push(x) -- Push element x to the back of queue.
# 
# 
# pop() -- Removes the element from in front of queue.
# 
# 
# peek() -- Get the front element.
# 
# 
# empty() -- Return whether the queue is empty.
# 
# 
# Notes:
# 
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).
# 
# 
#
from collections import deque

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        return self.q.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.q.popleft()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.q[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.q
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
