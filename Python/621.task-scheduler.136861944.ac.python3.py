#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (42.35%)
# Total Accepted:    31.2K
# Total Submissions: 73.6K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a char array representing tasks CPU need to do. It contains capital
# letters A to Z where different letters represent different tasks.Tasks could
# be done without original order. Each task could be done in one interval. For
# each interval, CPU could finish one task or just be idle.
# 
# However, there is a non-negative cooling interval n that means between two
# same tasks, there must be at least n intervals that CPU are doing different
# tasks or just be idle. 
# 
# You need to return the least number of intervals the CPU will take to finish
# all the given tasks.
# 
# Example 1:
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# 
# 
# 
# Note:
# 
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
# 
# 
#
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        res = 0
        stat = Counter(tasks)
        while len(stat) >= n + 1:
            tmp = sorted(list(stat.items()), key=lambda x: x[1], reverse=True)
            for i in range(n + 1):
                task, occur = tmp[i]
                if occur == 1:
                    del stat[task]
                else:
                    stat[task] -= 1
            res += n + 1
        occurs = list(stat.values())
        if not occurs:
            return res
        else:
            max_occur = max(occurs)
            res += (max_occur - 1) * (n + 1) + occurs.count(max_occur)
            return res
