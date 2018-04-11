#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (62.25%)
# Total Accepted:    109.2K
# Total Submissions: 175.5K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
# 
# 
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
# 
# 
# Follow up:
# 
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount  in c++ or in any other language.
# 
# 
# 
# Credits:Special thanks to @ syedee  for adding this problem and creating all
# test cases.
#
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        current = [1]
        res = [0, 1]
        rounds = len(bin(num)) - 3
        for i in range(rounds):
            current += [v + 1 for v in current]
            res += current
        return res[:num + 1]
