#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (37.76%)
# Total Accepted:    107.6K
# Total Submissions: 284.9K
# Testcase Example:  '1'
#
# 
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# 
# 
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
# return 2 because 13 = 4 + 9.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt
